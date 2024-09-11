<div align="center">
  Discord Bot: Identify Harmful messages by ChatGPT LLM.
  <br />
  <br />
</div>

<div align="center">
<br />

[![license](https://img.shields.io/github/license/dec0dOS/amazing-github-template.svg?style=flat-square)](LICENSE)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
    - [Manual setup](#manual-setup)
    - [Environment variables](#environment-variables)
- [License](#license)

</details>

---

## About

<table>
<tr>
<td>

It's a Discord bot designed to identify harmful messages using a ChatGPT. 
The bot listens to messages in Discord channels and categorizes them based on their content. If a message is identified as harmful, it is further classified into specific harmful categories and stored in a database for further analysis.

The bot is designed to help maintain a safe and healthy environment in Discord communities by automatically identifying and categorizing harmful messages, allowing for timely intervention and analysis.

</td>
</tr>
</table>

### Built With

The project uses these technologies:
- **Discord.py**: A Python wrapper for the Discord API, enabling the bot to interact with Discord servers and process messages.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) library for Python, used to interact with the database where harmful messages are stored.
- **Pandas**: A powerful data manipulation and analysis library for Python, used to process and analyze the data collected by the bot.
- **Logging**: Python's built-in logging module is used to track the bot's activities and debug issues.
- **BAML**: A library for managing and generating code, ensuring that the bot's codebase remains clean and maintainable.
- **Marshmallow**: A library for object serialization and deserialization, used to convert database entities to and from Python objects.


## Getting Started

### Prerequisites

It is recommended to use VS Code or Cursor for this project.
Python version that was used to develop the project: **3.9.13**

### Usage

#### Manual setup

Please follow these steps for manual setup:
1. Download this GitHub repository.
2. Create a virtual environment.

```
python3 -m venv <myenvname>
```

3. Activate virtual environment.

```
cd venv
Scripts\Activate.ps1
```
Or different Activate script, if you are not working from Visual Code.

4. Install packages from requirements.txt

```
pip install -r /path/to/requirements.txt
```

5. Replace environment variables with your PostgreSQL/Discord API credentials in the .env file.<br>
   **Replace ```CURRENT_ENVIRONMENT_NAME``` to use a correct environment (DEV for local machine, TEST for testing, PROD for AWS)**

6. Replace OPENAI_API_KEY in the baml_src/clients.baml with your own API KEY.

7. (Optional) Install BAML Visual Code extension [link](https://marketplace.visualstudio.com/items?itemName=Boundary.baml-extension)
This is super usefull if you're working with Visual Studio Code/Cursor IDEs.

We are using BAML library for working with Chat-GPT and other LLMs, enabling type-safety and rapid prototyping.
More about BAML - [here](https://github.com/BoundaryML/baml).

8. CD into /app to generate .BAML code from the baml_src.

```
cd app
```

9. Generate Python code from .BAML files.

```
baml-cli generate
```

This should create a folder baml_client with all of the python includes.

10. Run the app.

#### Deploying to AWS

1. Make sure the program works, run at least once to check if the discord bot is running.
2. In the ```.env``` file, change the ```CURRENT_ENVIRONMENT_NAME``` variable to use ```PROD``` .
3. Run Docker command from the terminal to build an image:
```
docker build -t questions-answer-matcher-container .
```
4. Run AWS CLI command to push the Docker Image:
```
aws lightsail push-container-image --service-name question-answer-matcher-service --label questions-answer-matcher-container --image questions-answer-matcher-container
```
5. Change the ```containers.json``` in the app directory to use the latest image
```
question-answer-matcher-service.questions-answer-matcher-prodX.X
```
6. Create an AWS deployment like this:
```
aws lightsail create-container-service-deployment --service-name question-answer-matcher-service --containers file://containers.json
```
7. Check AWS Web UI for any errors.

#### Environment variables

in the .env file, replace these environment variables with your PostgreSQL database credentials.

| Name                       |  Description                                                                 |
| -------------------------- | ---------------------------------------------------------------------------  |
| (TEST/DEV/PROD)_POSTGRES_DB_USER_NAME      | Database user name                                                           |
| (TEST/DEV/PROD)_POSTGRES_DB_PASSWORD       | Database password                                                            |
| (TEST/DEV/PROD)_POSTGRES_DB_URL            | URL of the PostgreSQL DB server                                              |
| (TEST/DEV/PROD)_POSTGRES_DB_URL_PORT       | URL Port                                                                     |
| (TEST/DEV/PROD)_POSTGRES_DB_NAME           | Database name                                                                |
| (TEST/DEV/PROD)_POSTGRES_DATABASE_URL      | A full replaced PostgreSQL DB URL for connection (DEV, TEST, PROD)             |
| DISCORD_API_BOT_TOKEN      | Discord Bot's TOKEN                                                          |
| CURRENT_ENVIRONMENT_NAME   | Indicates what environment to use (DEV, TEST, PROD)                          |

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.