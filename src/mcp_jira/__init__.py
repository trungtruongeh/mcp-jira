import argparse
from .server import mcp

def main():
    """MCP Jira: Read and Create your Jira tickets"""

    parser = argparse.ArgumentParser(
        description="Give you ability to read and create Jira tickets"
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()
