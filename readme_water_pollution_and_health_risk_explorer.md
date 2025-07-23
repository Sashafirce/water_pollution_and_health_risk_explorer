<p align="center">
  <img src="water_pollution_and_ health_ risk_ explorer.jpg" 
</p>

## WATER POLLUTION AND HEALTH RISK EXPLORER


Project XYZ is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualisation. The tool supports multiple data formats and provides an intuitive interface for both novice and expert data scientists.
CI logo
Dataset Content

    Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size of 100Gb.

Business Requirements

    Describe your business requirements

Hypothesis and how to validate?

    List here your project hypothesis(es) and how you envision validating it (them)

Project Plan

    Outline the high-level steps taken for the analysis.
    How was the data managed throughout the collection, processing, analysis and interpretation steps?
    Why did you choose the research methodologies you used?

The rationale to map the business requirements to the Data Visualisations

    List your business requirements and a rationale to map them to the Data Visualisations

Analysis techniques used

    List the data analysis methods used and explain limitations or alternative approaches.
    How did you structure the data analysis techniques. Justify your response.
    Did the data limit you, and did you use an alternative approach to meet these challenges?
    How did you use generative AI tools to help with ideation, design thinking and code optimisation?

Ethical considerations

    Were there any data privacy, bias or fairness issues with the data?
    How did you overcome any legal or societal issues?

Dashboard Design

    List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
    Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
    How were data insights communicated to technical and non-technical audiences?
    Explain how the dashboard was designed to communicate complex data insights to different audiences.

Unfixed Bugs

    Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
    Did you recognise gaps in your knowledge, and how did you address them?
    If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

Development Roadmap

    What challenges did you face, and what strategies were used to overcome these challenges?
    What new skills or tools do you plan to learn next based on your project experience?

Deployment
Heroku

    The App live link is: https://YOUR_APP_NAME.herokuapp.com/
    Set the runtime.txt Python version to a Heroku-20 stack currently supported version.
    The project was deployed to Heroku using the following steps.

    Log in to Heroku and create an App
    From the Deploy tab, select GitHub as the deployment method.
    Select your repository name and click Search. Once it is found, click Connect.
    Select the branch you want to deploy, then click Deploy Branch.
    The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
    If the slug size is too large then add large files not required for the app to the .slugignore file.

Main Data Analysis Libraries

    Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

Credits

    In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
    You can break the credits section up into Content and Media, depending on what you have included in your project.

Content

    The text for the Home page was taken from Wikipedia Article A
    Instructions on how to implement form validation on the Sign-Up page was taken from Specific YouTube Tutorial
    The icons in the footer were taken from Font Awesome

Media

    The photos used on the home and sign-up page are from This Open-Source site
    The images used for the gallery page were taken from this other open-source site

Acknowledgements (optional)

    Thank the people who provided support through this project.

About
No description, website, or topics provided.
Resources
Readme
Activity
Custom properties
Stars
2 stars
Watchers
2 watching
Forks
11 forks
Report repository
Releases
No releases published
Packages
No packages published
Footer

## Template Instructions

Welcome,

This is the Code Institute student template for the Data Analytics capstone project. We have preinstalled all of the tools you need to get started. It's perfectly okay to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo. Click the **Use this template** button, then click **Create a new repository**.

1. Copy the URL of your repository to your clipboard.

1. In VS Code, select **File** -> **Open Folder**.

1. Select your `vscode-projects` folder, then click the **Select Folder** button on Windows, or the **Open** button on Mac.

1. From the top menu in VS Code, select **Terminal** > **New Terminal** to open the terminal.

1. In the terminal, type `git clone` followed by the URL of your GitHub repository. Then hit **Enter**. This command will download all the files in your GitHub repository into your vscode-projects folder.

1. In VS Code, select **File** > **Open Folder** again.

1. This time, navigate to and select the folder for the project you just downloaded. Then, click **Select Folder**.

1. A virtual environment is necessary when working with Python projects to ensure each project's dependencies are kept separate from each other. You need to create your virtual environment, also called a venv, and then ensure that it is activated any time you return to your workspace.
Click the gear icon in the lower left-hand corner of the screen to open the Manage menu and select **Command Palette** to open the VS Code command palette.

1. In the command palette, type: *create environment* and select **Python: Create Environment…**

1. Choose **Venv** from the dropdown list.

1. Choose the Python version you installed earlier. Currently, we recommend Python 3.12.8

1. **DO NOT** click the box next to `requirements.txt`, as you need to do more steps before you can install your dependencies. Click **OK**.

1. You will see a `.venv` folder appear in the file explorer pane to show that the virtual environment has been created.

1. **Important**: Note that the `.venv` folder is in the `.gitignore` file so that Git won't track it.

1. Return to the terminal by clicking on the TERMINAL tab, or click on the **Terminal** menu and choose **New Terminal** if no terminal is currently open.

1. In the terminal, use the command below to install your dependencies. This may take several minutes.

 ```console
 pip3 install -r requirements.txt
 ```

1. Open the `jupyter_notebooks` directory, and click on the notebook you want to open.

1. Click the **kernel** button and choose **Python Environments**.

Note that the kernel says `Python 3.12.8` as it inherits from the venv, so it will be Python-3.12.8 if that is what is installed on your PC. To confirm this, you can use the command below in a notebook code cell.

```console
! python --version
```

## Deployment Reminders

* Set the `.python-version` Python version to a [Heroku-22](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version that closest matches what you used in this project.
* The project can be deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the **Deploy** tab, select **GitHub** as the deployment method.
3. Select your repository name and click **Search**. Once it is found, click **Connect**.
4. Select the branch you want to deploy, then click **Deploy Branch**.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button **Open App** at the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the `.slugignore` file.
