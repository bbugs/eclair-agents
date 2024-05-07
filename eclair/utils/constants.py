from typing import List

SYSTEM_PROMPT: str = "You are a helpful assistant that automates digital workflows."

EXECUTORS: List[str] = [
    "text_mike",
    "text_avanika",
    "vision_mike",
    "vision_avanika",
    "uni_mike",
    "vision_avanika_no_validation",
    "vision_executor_l1",
    "vision_mike_no_validation",
    "vision_executor_l2",
]

TASK_LIST = {
    "gmail-1": 'In my personal Gmail, move all messages that were sent from "Deep (Learning) Focus" to the folder "DL Newsletters"',
    "gmail-2": 'In my personal Gmail, change my Settings to enable the Advanced "Template" feature for saving email templates.',
    "gmail-3": 'In my personal Gmail, reply "hi" to the first unread message in the "Tickets" folder',
    "gmail-4": "In my personal Gmail, create an event (dinner @ flour and water in SF) on my gmail calendar for 7:00PM on November 3rd. Invite ashraynarayan0@gmail.com",
    "outlook-1": "In my Outlook, Save an email draft to kristaoo@stanford.edu asking for her Doordash food order.",
    "outlook-2": "In my Outlook, change my Settings to switch the text size to Small.",
    "outlook-3": 'In my Outlook, create a New Event called "Test Event" in my Calendar for November 7th, 2023 bewteen 11am-1pm',
    "outlook-5": "Send an emai to avanika@cs.stanford.edu asking for a product update. Make sure the email has a subject",
    "outlook-6": "create a dinner event on my outlook calendar for 7:00PM on Oct 30th. Invite ashraynarayan0@gmail.com",
    "outlook-7": "Reply to the email from Chris, saying: Got it! This was really helpful. Thanks so much for your help. Best, Avanika (sent using Eclair)",
    "outlook-8": "Write an email to avanika@cs.stanford.edu asking for a project update. Make sure the email has a subject",
    "google_drive-1": 'Create a new google document, title it "Essay Draft", and add a bolded title to the body with the text "Civil War Analysis"',
    "google_drive-2": 'Delete the folder titled "ML research ideas"',
    "google_drive-3": 'Create a new folder titled "ML research ideas" and share with avanikan@cs.stanford.edu',
    "doordash-1": "Order me 10 of the hunter pence, 5 of the paul reuben, 5 of the matt cain and and 8 of the strawberry girls sandwhices from Ike's Love & Sandwiches",
    "doordash-2": "Order me 10 veggie super burritos, 10 chicken super burritos, and 10 steak super burritos from El Grullense on Doordash",
    "doordash-3": "Order me a Jasmine Green Tea from Teaspoon on Doordash",
    "doordash-4": 'place a delivery order for a bagel from a restaurant that can deliver in "Under 30 min"',
    "doordash-5": 'create a Pickup order for one "Hash Brown" from Jack in the Box',
    "opentable-1": "Book me a reservation at Camper around 7:30PM for 2 people",
    "opentable-2": "Book me a table at Zuni Cafe on Nov 12 @ 830PM for 2 people. reservation name is Avanika Narayan, and my phone number is 4089819553. email is gostanfordtennis@gmail.com",
    "opentable-3": "Book me a table at Che Fico San Francisco on Nov 15 @ 8:30PM for 2 people. reservation name is Avanika Narayan, and my phone number is 4089819553. email is gostanfordtennis@gmail.com",
    "opentable-4": "Using opentable book me a table at Arabian Knights in palo alto @ 10:30PM",
    "opentable-5": "Book a table @ Camper in Menlo Park for 4 people @ 7:30PM on November 10th",
    "opentable-6": "Book a table @ Camper in Menlo Park for 4 people @ 7:30PM on November 7th. Make the reservation under the name: Avanika Narayan, email: gostanfordtennis@gmail.com, phone: 4089819553",
    "opentable-7": "Make a reservation at an Italian restaurant with at least 4 stars for 2 people on November 10th at 8pm",
    "farfetch-1": "Find me a Thom Browne sweater. first find sweaters, then order it in a size 2",
    "resy-1": "Using Resy.com book me a table at mission chinese food in SF @ 10PM",
    "nike-1": "Buy me a pair of Nike SB Zoom Nyjah's in size 9.5",
    "southwest-1": "Search for all southwest flights from SJC to MSY departing on 11/10 and returning on 11/16.",
    "google_maps-1": "Get me directions to flour and water in SF from the Stanford Quad",
    "slack-1": 'Create a new private channel labeled named "test"',
    "slack-2": "Send a private message to Michael Wornow asking about meeting times tomorrow",
    "slack-3": 'Copy the contents of the last message in the channel "jarvis" and paste it into a private message to Michael Wornow',
}
