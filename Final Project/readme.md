**NAMES OF COLLABORATORS HERE**
Big Coop (CJM424@cornell.edu), Jacob Everly (je354@cornell.edu)

## Project Plan can be found on this notion:
https://www.notion.so/martineckardt/IDD-Final-Project-Physical-Bound-Tokens-06b33dad5666426f9ae2378c47a4595d

## Design Process

Design Overview of how the whole system generates reports, scans and gives out keys:

![Note Nov 28, 2022](https://user-images.githubusercontent.com/112036223/205974335-43f136e9-e9ec-4a96-b218-fb4089cf2d26.jpg)

The overview of the Cryptographic ideas used in generating keys and verifying reports:

![Screenshot 2022-12-06 115915](https://user-images.githubusercontent.com/112036223/205975029-1821e5d0-c007-4e22-9f27-4ec91ac54637.png)


The UX of the report that is generated:

![IMG_4449](https://user-images.githubusercontent.com/112036223/205974551-6aca144e-5346-40c4-8459-a12d5a8110dc.jpeg)



Here is the story board that would be the ideal interaction of a succesful package being delivered. Note at the edn once the report is verified in the smart contract. The assest on chain is automatically moved to the next owners wallet and payment is processed instantly.

![Copy of Note Nov 29, 2022](https://user-images.githubusercontent.com/112036223/205970907-e0778724-4273-4379-9f92-fd699730b72f.jpg)

Storyboard showing the package going above the temperture agreed upon all the parties for a temperature sensitive package:

![Screenshot 2022-12-06 121805](https://user-images.githubusercontent.com/112036223/205978939-1ac5100b-80b0-4b9f-9062-784e4930072c.png)


Storyboard showing the package reaching the threshold of accelaration agreed upon the two parties for a fragile package:

![Note Nov 29, 2022 (2)](https://user-images.githubusercontent.com/112036223/205971469-3cbad939-2d9a-4a3d-bc0d-2eed2ea74bc7.jpg)

Picture of the prototype being put together:

The system consisted of the raspberyy pi, gyro, temp sensor, nfc writer, external battery pack:

![Screenshot 2022-12-06 120501](https://user-images.githubusercontent.com/112036223/205976213-e4d11cb7-6bc0-44cb-9931-2f03d3eaa8df.png)


![Screenshot 2022-12-06 120622](https://user-images.githubusercontent.com/112036223/205976489-7fe61820-7d7b-42c5-b721-4aeaf978f5fe.png)


![Screenshot 2022-12-06 120700](https://user-images.githubusercontent.com/112036223/205976594-a96f82aa-a6c5-4be0-b094-2ae51bd4e9fb.png)



## Functioning Project

Code for the project is in the following files:

Code that has the library for the NFC reader and writer to be translated from C to Python so our Pi can interact with the writer. Also has the correct protocol for an iphone to be able to read the chip.

https://github.com/JacobEverly/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/adafruit_st25dv16.py

Code that generates the report and writes it to the NFC chip for the scanner to read:

https://github.com/JacobEverly/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/writer.py

Code that creates the Private and Public Keys and makes the database that is able to verifty the reports authenticity:

https://github.com/JacobEverly/Interactive-Lab-Hub/blob/Fall2022/Final%20Project/verifier.py

Video of the reports being Generated Properly



https://user-images.githubusercontent.com/112036223/205968464-9f75841c-ee38-4975-8290-1de0c72a671e.mov


Video of a report being verified



https://user-images.githubusercontent.com/112036223/205968704-84977046-f95a-4536-b7a4-6a09e5f0b2b9.mov


Video of a report being denied due to the wrong signature being provided



https://user-images.githubusercontent.com/112036223/205968848-76414c57-22be-47b4-af8e-965002b6218d.mov


# Interactions with User

Video of the package being delivered


https://drive.google.com/drive/folders/11y1TmAnFA99VmxU-SccPMnDfu82Z8mN5?ths=true


Video of the package being delivered and being dropped

https://drive.google.com/drive/folders/11y1TmAnFA99VmxU-SccPMnDfu82Z8mN5?ths=true


# Final Reflections

In our project, we built a physical device that mimics a device that could work with a blockchain and make sure the confirmation of supply chain requirements is immutable. This device is capable of reading and writing data to a blockchain, as well as performing cryptographic operations. We achieved all of the objectives we wanted to, including sensor readings and proper security measures. Through this physical device, we have made a significant stride towards providing a reliable and secure link between the physical world and a blockchain. However, one challenge that we faced was making the device easy to use for everyday users.

 To make the device more user-friendly, there are several things that could be done. These include reducing the complexity of the interface, providing users with an easy-to-understand tutorial, and having a dedicated support system for users who are having difficulty operating the device. Additionally, providing users a visually appealing user interface would help users understand the device more easily and make it more enjoyable to use. We could also create a mobile application to provide users with access to the device’s functions. Lastly, we could make sure the device is compatible with various operating systems and blockchain networks to ensure wider usability. 

In order to use the device, it is essential that it is scanned using an NFC reader. This will execute the smart contract on the blockchain, allowing users to securely unlock the device and verify the identity of the user. This step is necessary to ensure the safety of the device and the data stored on it. With this in mind, we need to make it clear to users that they must use an NFC reader to activate the device and initiate the smart contract. This will help guarantee that the device is secure and that the data on the blockchain is immutable.

The app we create should allow users to access the device's functions with minimal input. We should also design the app with enough information for users to understand that the system is working properly. This could include a tutorial on how to use the device, real-time updates on the status of the device, and visual indicators to show the user when the device is working correctly. By taking these steps, we can ensure that the device is easy to use, secure, and reliable.

Also to make the device more user friendly, we could look into automating the application process so that the user would not have to take the responsibility for the entire process. Automating the application process would allow for the device to automatically read the data from the sensors and write it to the blockchain, thus eliminating any potential user error. Additionally, automating the application process would also shorten the time it takes for the device to read and write data, thus making the device more efficient. Ultimately, automating the application process would make the device much easier to use, while also improving its efficiency and reliability.

We think next we should test considering the following two designs. The minimal interaction design would ensure that the user does not need to understand the technicalities of the device or the blockchain, but it could lead to users making decisions that do not align with their desired outcomes. On the other hand, the more complicated design could provide users with a better understanding of their actions and the consequences of these actions, but this could be more difficult for the user to understand and use. We have to take into account the user’s experience when designing the device. 

Through careful testing of the device’s user interactions, we can ensure that users are able to make informed decisions and understand the implications of their actions. This will help us create a device that is both secure and user friendly, allowing users to enjoy using the device while also providing the necessary security measures. Furthermore, since we are in the unique position of providing a B2B service, training can be done more easily to ensure users have the necessary knowledge to use the device.

# Group work distribution questionnaire

All teamates feel that everyone contributed equal time and value to the projects final outcome. In generall the roles were as follwing

Martin ( Cryptography and Blockchain )
Cooper ( Tech stack and NFC lead )
Jacob ( Fabrication and Hardware Stack )

Before the project began the team met and established goals and expectations for everyone and these were all met throughout the project's lifetime.
