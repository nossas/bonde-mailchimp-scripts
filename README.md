# Bonde Mailchimp Script

Scripts based on Python 3 to manage lists in [Mailchimp](https://developer.mailchimp.com/documentation/mailchimp/).

## Getting Started

First you'll need to get the source of the project. Do this by cloning the whole repository:

```
git clone https://github.com/nossas/bonde-mailchimp-scripts.git
cd bonde-mailchimp-scripts
```

It is good idea (but not required) to create a virtual environment for this project. We'll do this using [venv](https://docs.python.org/3/library/venv.html) module that built-in in Python3 to keep things simple, but you may also find something like [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) to be useful:

```
python3 -m venv env
source env/bin/activate
```

Now we can install our dependencies:

```
pip install -r requirements.txt
```

## Run scripts


### Scripts to manage members

**CLI**

`python scripts/members.py [OPTIONS] [COMMAND]`

**Commands**

- `unsubscribed`
- `delete`

**Arguments**

- `--token`: Mailchimp api token, is required.
- `--list_id`: List ID of Mailchimp group, is required.
- `--member_id`: Member ID of Mailchimp list, required only when there is no input --csv
- `--csv`: CSV file with email of member on first column, required only when there is no input --member_id


> **IMPORTANT:** The CSV file used must contain the member's email in the first column, and should not have header in the first line.