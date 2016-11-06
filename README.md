# Email

Have you ever had to send the same email to each person individually? There are many reasons for doing so. For example, when an email requires a more personal touch or when the email conversation cannot be shared. `sendEmail.py` is a script that allows you to send the same email to multiple recepients separately and address each recepient by their respective names. This is more efficient than composing and sending a new message repeatedly for each recepient!

# Input
The script `sendEmail.py` requires an input file for email specifications and another input file containing the body of the text itself. 

### Specification file
In the specification file, the user will fill out the following fields. Information for each field should be filled to the right of `=` and multiple items should be separated by `,`. No spaces should be used in the specification file unless it is part of the information. In the specification file, the fields are:

1. `account`: email address sending the email.
2. `password`: password for email account sending email.
3. `sender`: user's registered name in email account.
4. `addresses`: email addresses to send to.
5. `subject`: title of the email.
6. `attachments` [optional]: locations to attachment.
7. `recepients`: names of receipients, with each name used in the body of each receipient email in the order that receipient emails are listed for `addresses`.

If no attachments are available, then it is okay to leave the space to the right of `=` for `attachments` blank. Below is an example of how to fill out the specification file. Note that the field names should not be modified.

<br>
<img height = "200" width = "400" src = "https://github.com/CalvinTChi/Email/blob/master/pic1.png" />
<br>

The the example in the picture, there are two receipients and each email will have two attachments. 

### Body
The body of the text should be typed into a text file the same way it would be typed when composing a regular email with one exception - the name of the recepient must be substituted with a `%s`. This is important as `sendEmail.py` will replace `%s` with the name of the recepient specified in the specification file. An example of what a text file containing the body of the email would look like is below:

<br>
<img height = "200" width = "650" src = "https://github.com/CalvinTChi/Email/blob/master/pic2.png" />
<br>

Rest assured that the plain text formatting (i.e. spaces, newlines) in the body text file will be reflected in the email.

# Usage
Finally, when the two input files are ready, the usage is:

`python sendEmail.py -s <specification> -b <body>`

Where `<specification>` refers to specification file and `<body>` refers to text file containing body of the email. 
