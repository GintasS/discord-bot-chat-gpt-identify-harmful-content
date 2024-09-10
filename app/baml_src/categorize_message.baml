enum HarmfulMessageCategory {
  HarrassmentAndBullying 
  HateSpeech
  TrollingAndBaiting
  NSFW
  Spam
  MisinformationAndDisinformation
  DoxxingAndPrivacyViolation
  IllegalActivities
  Other
}

function ExtractMessageCategoryFromMessage(message : string) -> HarmfulMessageCategory {
  client GPT4oMini
  prompt #"
    Extract a message category from this message:
    {{ message }}

    {{ ctx.output_format }}
  "#
}

test test_message1 {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "You're a loser"
  }
}

test test_message2 {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "Gays are disgusting"
  }
}

test test_message3 {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "The goverment of Lithuania is a communist goverment"
  }
}

test test_message4 {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "I want to suck you"
  }
}

test test_message5 {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "Buy my new iphone case! It is really good. Buy my new iphone case"
  }
}

test test_message6 {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "The moon landing was a fake one, don't believe that guys"
  }
}

test test_message7 {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "Hey guys, that person address is 222 test street, Lithuania"
  }
}

test test_message8 {
  functions [ExtractMessageCategoryFromMessage]
  args {
    message "Hey, anyone of you are interested in pirated games?"
  }
}


