import requests
import json
import os

token = "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"
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github+json',
}

repo_url = "https://api.github.com/repos/miralireza/MaktabsharifMiniProject3"
branches_url = f"{repo_url}/branches"

response = requests.get(branches_url, headers=headers)
print("Branches Response:", response.status_code)

if response.status_code != 200:
    print("Failed to get branches:", response.status_code, response.text)
    exit()

branches = response.json()

if not os.path.exists('commits'):
    os.makedirs('commits')

processed_commits = []

for branch in branches:
    branch_name = branch['name']
    print("Processing Branch:", branch_name)

    commits_url = f"{repo_url}/commits?sha={branch_name}"
    response = requests.get(commits_url, headers=headers)
    print("Commits Response:", response.status_code)

    if response.status_code != 200:
        print("Failed to get commits:", response.status_code, response.text)
        continue

    commits = response.json()

    for commit in commits:
        commit_sha = commit['sha']

        if commit_sha in processed_commits:
            continue

        processed_commits.append(commit_sha)
        committer_name = commit['commit']['committer']['name']
        print("Processing Committer:", committer_name)

        filename = f"commits/{committer_name.replace(' ', '_')}.json"
        with open(filename, 'a') as f:
            f.write(json.dumps(commit, indent=4) + '\n')
        print(f"Commit from {committer_name} saved to {filename}")
