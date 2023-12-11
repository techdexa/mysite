# -*- coding: utf-8 -*-
import subprocess

def clone_repos_from_file(file_path):
    with open(file_path, 'r') as file:
        repo_urls = file.read().splitlines()

    for repo_url in repo_urls:
        clone_repo(repo_url)

def clone_repo(repo_url):
    try:
        subprocess.run(['git', 'clone', repo_url])
        print(f"Repository cloned: {repo_url}")
    except Exception as e:
        print(f"Error cloning repository {repo_url}: {e}")

# Example usage
file_path = 'githubandroidkotlin.txt'  # Replace with the actual path to your repo list file
clone_repos_from_file(file_path)
