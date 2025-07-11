const { spawn } = require("child_process");
const os = require("os");
const path = require("path");
const fs = require("fs");

function getBinaryPath(baseDir) {
  const platform = os.platform();

  if (platform === "win32") {
    return path.join(baseDir, "main.exe");
  } else if (platform === "darwin") {
    return path.join(baseDir, "main.bin");
  } else {
    return path.join(baseDir, "main");
  }
}

function ensureExecutable(filePath) {
  const platform = os.platform();
  if (platform === "win32") {
    // Windows не использует chmod +x
    return;
  }

  try {
    const stat = fs.statSync(filePath);

    // Если файл уже исполняемый, ничего не делаем
    if (stat.mode & 0o111) {
      return;
    }

    // Устанавливаем +x (исполняемый для владельца, группы, всех)
    fs.chmodSync(filePath, stat.mode | 0o111);
  } catch (err) {
    console.error("Failed to set +x on binary:", err);
    process.exit(1);
  }
}

// Получаем аргументы
const allArgs = process.argv.slice(2);

if (allArgs.length < 1) {
  console.error("Usage: node launcher.js <binary-dir> [args...]");
  process.exit(1);
}

const binaryDir = allArgs[0];
const binaryArgs = allArgs.slice(1);
const binaryPath = getBinaryPath(binaryDir);

// Убедиться, что бинарь исполняемый
ensureExecutable(binaryPath);

// Запуск
const child = spawn(binaryPath, binaryArgs, {
  stdio: ["pipe", "pipe", "pipe"],
});

process.stdin.pipe(child.stdin);
child.stdout.pipe(process.stdout);
child.stderr.pipe(process.stderr);

child.on("exit", (code) => {
  process.exit(code);
});

child.on("error", (err) => {
  console.error("Failed to start binary:", err);
  process.exit(1);
});