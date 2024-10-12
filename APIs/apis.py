import os
import asyncio
import random
from datetime import datetime, timedelta

# Define the languages and output directories for each.
languages = {
    "java": "java-client",
    "cpp-qt-client": "cpp-qt-client",
    "javascript": "javascript-client",
    "python-aiohttp": "python-aiohttp-client"
}

# Set a limit for concurrent subprocess executions
CONCURRENCY_LIMIT = 10
semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

async def run_subprocess(command):
    """Runs a subprocess asynchronously with a concurrency limit."""
    async with semaphore:
        process = await asyncio.create_subprocess_exec(
            *command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            print(f"Error: {stderr.decode().strip()}")
        return stdout.decode().strip()

async def branch_exists(branch_name):
    """Check if a Git branch already exists."""
    result = await run_subprocess(["git", "branch", "--list", branch_name])
    return bool(result.strip())

async def checkout_or_create_branch(branch_name):
    """Switch to the correct branch if it exists, otherwise create a new one."""
    if await branch_exists(branch_name):
        print(f"Switching to existing branch {branch_name}")
        await run_subprocess(["git", "checkout", branch_name])
    else:
        print(f"Creating and switching to new branch {branch_name}")
        await run_subprocess(["git", "checkout", "-b", branch_name])

async def commit_changes(branch_name):
    """Asynchronously commit changes to the current branch."""
    # Simulate random commit time between 2 years ago and now
    now = datetime.now()
    two_years_ago = now - timedelta(days=730)
    random_time = two_years_ago + timedelta(
        seconds=random.randint(0, int((now - two_years_ago).total_seconds()))
    )
    commit_time_str = random_time.strftime('%Y-%m-%dT%H:%M:%S')
    
    # Git operations
    await run_subprocess(["git", "add", "."])
    await run_subprocess([
        "git", "commit", 
        "-m", f"Generated client code for {branch_name}", 
        "--date", commit_time_str
    ])

async def generate_client_code(openapi_file, subdir, lang, out_dir):
    """Asynchronously generate client code for a given language."""
    output_dir = os.path.join(subdir, out_dir)
    command = [
        "openapi-generator", "generate",
        "-i", openapi_file,
        "-g", lang,
        "-o", output_dir
    ]
    await run_subprocess(command)

async def process_language(openapi_file, subdir, lang, out_dir):
    """Handles branch creation or switching, client generation, and committing."""
    branch_name = f"{lang}_client_branch"
    
    print(f"Checking out or creating branch {branch_name} for {lang}")
    await checkout_or_create_branch(branch_name)

    print(f"Generating {lang} client code for {openapi_file}")
    await generate_client_code(openapi_file, subdir, lang, out_dir)
    
    print(f"Committing changes to branch {branch_name}")
    await commit_changes(branch_name)

async def process_openapi_file(openapi_file, subdir):
    """Asynchronously processes an OpenAPI file, generating clients for all languages."""
    tasks = []
    for lang, out_dir in languages.items():
        tasks.append(process_language(openapi_file, subdir, lang, out_dir))

    # Run all language processing tasks concurrently, but with the semaphore limit
    await asyncio.gather(*tasks)

async def traverse_and_generate_clients(root_dir):
    """Asynchronously traverses the directory and processes OpenAPI files."""
    tasks = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".yaml"):
                openapi_file = os.path.join(subdir, file)
                tasks.append(process_openapi_file(openapi_file, subdir))

    # Process all OpenAPI files concurrently, but respecting the semaphore limit
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    root_directory = "/home/spocam/Desktop/openapi-directory/APIs/"
    
    # Run the asynchronous traversal and generation
    asyncio.run(traverse_and_generate_clients(root_directory))
