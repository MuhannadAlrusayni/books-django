Challenge: Custom Django Admin Interface for a ‘Book’ Model
Objective:
Create a Django project with a custom admin interface for a model named Book.
Requirements:

Model Creation:
	•	Create a Book model with fields: title (CharField), author (CharField), published_date (DateField), genre (CharField), and rating (IntegerField).
	•	Create a related Review model with fields: reviewer_name (CharField), comment (TextField), and date (DateField). This should be related to the Book model.
Admin Interface Customization:
	•	Customize the list display to show all fields of the Book model.
	•	Implement a search feature for title and author.
	•	Add filters for genre and published_date.
	•	Customize the form to include a dropdown for genre and a date picker for published_date. Ensure rating is validated to be between 1 and 5.
	•	Implement the Review model as an inline in the Book admin page.
Additional Features:
	•	Add a custom action to export selected books’ details as a CSV file.
	•	Implement optimizations for handling large numbers of records. (not clear)
	•	Ensure all user inputs are properly sanitized for security.
	•	(Bonus) Display the rating field in the list display using stars instead of numbers.
Documentation & Testing:
	•	Provide clear documentation on setting up and testing the admin interface.
	•	Include tests to verify the functionality of your implementation.
Submission Instructions:
	•	Create a new GitHub repository for your project.
	•	Ensure your code is well-organized and includes comments where necessary.
	•	Include a README file with instructions on how to set up and run your project, along with any other relevant information.
	•	Once complete, please send us the link to your GitHub repository.