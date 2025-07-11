import sys

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Simple MCP Server")


@mcp.tool()
def sum_two(a: int, b: int) -> int:
    """
    Sums two integers.
    """
    return a + b


if __name__ == "__main__":
    print("Starting File Manager MCP Server...", file=sys.stderr)

    mcp.run()
