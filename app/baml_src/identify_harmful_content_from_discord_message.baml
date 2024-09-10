class IsHarmfulMessage {
  discord_message string @description("The original discord_message")
  is_harmful bool @description("True if the discord message is harmful, false otherwise")
}

function IdentifyHarmfulDiscordMessage(discord_message: string) -> IsHarmfulMessage {
  client GPT4oMini
  prompt #"
    Having this Discord Message: {{ discord_message }}
    Do you believe this is a harmful message?
    Harmful message means that the discord message falls into at least one of these categories: 
    harrassment and bullying, 
    hate speech, 
    trolling and baiting, 
    NSFW(not safe to work), 
    spam, 
    misinformation and disinformation, 
    doxxing and privacy violation,
    illegal activities
   
    Return the answer in the following format: 
    {{IsHarmfulMessage}}

    {{ ctx.output_format }}
  "#
}

test DiscordMessageIsHarmful {
  functions [IdentifyHarmfulDiscordMessage]
  args {
    discord_message "You piece of shit moderator",
    is_harmful "true"
  }
}

test DiscordMessageIsSafe {
  functions [IdentifyHarmfulDiscordMessage]
  args {
    discord_message "You are a very good moderator",
    is_harmful "false"
  }
}