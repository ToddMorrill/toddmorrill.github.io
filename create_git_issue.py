import os
import json
import requests
import argparse

parser = argparse.ArgumentParser(description='Login to github & create issue')
parser.add_argument('--username', default='tmorrill12@gmail.com',
    dest='username', help='github email address')
parser.add_argument('--password', dest='password',
                   help='github password')
parser.add_argument('--repo_owner', default='ToddMorrill',
    dest='repo_owner', help='github repo owner handle')
parser.add_argument('--repo_name', default='toddmorrill.github.io',
    dest='repo_name', help='github repo name')
parser.add_argument('--post_name', required=True,
    dest='post_name', help='full post filename (with .md)')


args = parser.parse_args()

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = args.username
PASSWORD = args.password

# The repository to add this issue to
REPO_OWNER = args.repo_owner
REPO_NAME = args.repo_name

def make_github_issue(title, body=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))

    # get the issue id to update the .md post with
    issue_number = r.json()["number"]

    # add this issue number to the front matter of the post .md file
    with open("./_posts/{}".format(args.post_name), "r") as f:
        file_contents = f.read()
    with open("./_posts/{}".format(args.post_name), "w") as f:
        file_contents = file_contents.split("\n")
        # find the second occurrence of "---", and use as your insertion point
        insert_line_num = [i for i, n in enumerate(file_contents) if n == "---"][1]
        file_contents.insert(insert_line_num, "commentIssueId: {}".format(issue_number))
        for line in file_contents:
            f.write(line+"\n")

    if r.status_code == 201:
        print ('Successfully created Issue {0:s}'.format(title))
    else:
        print ('Could not create Issue {0:s}'.format(title))
        print ('Response:', r.content)

if __name__ == '__main__':
    title = "comments for post: {}".format(args.post_name)
    body = "open issue for comments"
    
    make_github_issue(title=title, body=body)