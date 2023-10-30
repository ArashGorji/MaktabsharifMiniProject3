import requests
import json

def get_commits(username, repo, token = None):
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    headers = {"Authorization": f"Bearer {token}"}
    if token:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url)
    commits = response.json()
    return commits

def save_commits_to_file(commits, filename):
    with open(filename, 'w') as file:
        json.dump(commits, file, indent=4)

def main():
    username = 'ArashGorji'
    repo = 'MaktabsharifMiniProject3'
    token = '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'

    commits = get_commits(username, repo)
    save_commits_to_file(commits, 'commits.json')

if __name__ == "__main__":
    main()