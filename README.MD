## Reminder (CI/CD using AWS CodePipeline)

This is simple django project to send reminder email to patients at the scheduled time.
The purpose of this project is show how to implement CI/CD using AWS in django.

### Technical Stacks
+ Django
+ [Docker](/Dockerfile)
+ AWS CodePipeline
+ [AWS CodeBuild](/buildspec.yml)
+ AWS CodeDeploy
+ AWS ECS Fargate

### Preview
![Relevance feedback image](https://github.com/certainty15750/reminder/blob/master/Screenshots/IMG.png)
![Relevance feedback image](https://github.com/certainty15750/reminder/blob/master/Screenshots/IMG1.png)
![Relevance feedback image](https://github.com/certainty15750/reminder/blob/master/Screenshots/IMG2.png)
![Relevance feedback image](https://github.com/certainty15750/reminder/blob/master/Screenshots/IMG3.png)


### How to implement CI/CD
+ create CodePipeline on AWS
    + Code Source: Integrate github with CodePipeline
    + Code Build:  build code and deploy to ECR
    + Code Deploy: Update ECS service using ECR
    
  
### Contact Me
+ Name: Jason Halog
+ Email: certainty15750@yahoo.com


