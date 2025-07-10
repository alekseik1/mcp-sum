from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Simple MCP Server")


@mcp.tool()
def sum_two(a: int, b: int) -> int:
    """
    Sums two integers.
    """
    print("ХУЙ ПИЗДА СКОВОРОДА")
    return a + b


if __name__ == "__main__":
    mcp.run("sse")
