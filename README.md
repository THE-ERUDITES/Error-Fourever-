# Error-Fourever-
E-POLL - HACKBASH 2021 <br>
The idea of the project was to build an E-Voting System for conducting elections securely, easily and reliably. The importance of an online system clearly emerged during the pandemic when the number of covid cases increased in those states of India where elections were conducted through traditional methods at poll booths. Apart from pandemic times. The E-Voting System allows users to vote in their free time and from anywhere and there is reduced congestion.Moreover it becomes quite difficult to conduct general elections online, especially with proper verification of the voter in their absence. To facilitate this, we propose a feasible solution aiming to attain utmost security and verification including features such as email verification, OTP generation and face recognition.

There is a government database which contains the email-id of all voters along with their valid voter IDs. On landing upon the home page, a voter has options to check out the details of the candidates and to cast his vote. When the user decides to cast his vote, he/she needs to register himself with the email-id and voter ID in govt. Database and fill in other details like age and photo. Upon signing up, the user receives a verification mail.

Once an account is verified, the user can login. At this step, an OTP is sent via mail for authentication. The OTP expires once it is used. Now the user will be asked for face verification. The snapshot taken will be compared with the passport photo uploaded by them. If the photos are the same, it will be redirected to the Voting Page and if not, it will log the user out. This added authentication ensures that even if someone breached into a user's account with his credentials, they won't be able to cast their vote.

In the Admin's control panel, the admin can insert new candidates or update information of old candidates. Also admin can see the statistics of the election through graphs. It can be accessed only by person having admin login credentials. 

We have used PHPMailer for email-triggering. Also, whoever hosts the website should change google settings to allow less secure apps. 

Tech Stack used: PHP, SQL, HTML, CSS, BOOTSTRAP, PYTHON, DEEP LEARNING

