import os
import json
import requests
from datetime import datetime

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.getenv('GITHUB_PAT')}",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.get(
    url=f"https://api.github.com/orgs/{os.getenv('ORG')}/actions/runners", 
    headers=headers
)

runners = response.json()["runners"]

for runner in runners:
    print(f"checking: {runner['name']}")
    if runner["status"] == "offline":

        labeled = False
        for label in runner["labels"]:
            if label["name"].startswith("ts-"):
                labeled = True
                timestamp = datetime.fromtimestamp(int(label["name"].split("-")[1].split(".")[0])).timestamp()
                print(f"time diff: {datetime.now().timestamp() - timestamp}")
                if datetime.now().timestamp() - timestamp > 300:
                    response = requests.delete(
                        url=f"https://api.github.com/orgs/{os.getenv('ORG')}/actions/runners/{runner['id']}", 
                        headers=headers
                    )
                    print(response.status_code)

                continue

        if not labeled:
            label = f"ts-{datetime.now().timestamp()}"
            response = requests.post(
                url=f"https://api.github.com/orgs/{os.getenv('ORG')}/actions/runners/{runner['id']}/labels", 
                headers=headers,
                json={"labels": [ label ]}
            )
            