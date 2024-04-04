App Service: 
Azure App Service lets you create apps faster with a one-of-a kind cloud service to quickly and easily create enterprise-ready web and mobile apps for any platform or device and deploy them on a scalable and reliable cloud infrastructure.

Approx Monthly cost:

Pros:
High availability with SLA-backed uptime of 99.95 %.
It has built in infrastructure maintenance, scaling. 
Continuous Deployment workflow backed up with AzureRepos, GitHub, BitBucket.
It is simpler than VM.
 
Cons: 
Provides no control over the infrastructure
 
Virtual Machine:
 
It gives you the flexibility of virtualization without having to buy and maintain the physical hardware that runs it. However, you still need to maintain the VM by performing tasks, such as configuring, patching, and installing the software that runs on it.
 

Pros: 
It provides complete control over the infrastructure.
high availability with SLA-backed uptime of 99.5% 
can be scaled from one to thousands of VM instances. 
more customization of the app's capability.
 
Cons:
Increased Complexity compared to App Service
 
App Service: The costs, scalability, and availability for a CMS app deployed through an App Service are reasonable. This is a fairly lightweight app, so it does not need a significant compute capability. So even though the service plans are constant and the user is paying even when no one is accessing the service, the reduced compute requirements of a CMS app are not expensive. Continous deployment through GitHub workflows on the Azure portal makes updating the CMS app a snap. 
VM: The costs, scalability, and availability for a CMS app deployed through a VM are also reasonable. The VM allows for more customization of the app's capability. It also would really benefit developers who have already built a CMS app but it might not be supported through App Service but could work through the VM workflow. It also allows for more fine-tuning, so the developer can customize the VM to optimize their CMS app.
 
 
Decision:
Deployment option: App Service (https://cmsappazuretwo.azurewebsites.net/)
I chose App Service because the CMS app is lightweight, does not require much computing power, and is easy to deploy through Azure. The CMS App is straightforward and runs on a Python codebase, which is supported by App Service. Overall, a simple choice.
 
Assess app changes that would change your decision. 
Detail how the app and any other needs would have to change for you to change your decision in the last section.
 
Azure APP Service- If this application would need features that Azure does not provide then I would have to change my decision to VMs. In addition, if this application required more control of the hardware/infrastructure then I would also have to switch to VMs.
 
Azure Virtual Machines(VMs)- If this application had a decline in traffic then it's best to switch to App Service for more cost savings since high-performance computing would not be needed. Overall if there were budgeting constraints then moving the application to App Service would create cost savings. Lastly, if there are tight deadlines then moving to an App Service will reduce the time it takes to deploy an application.
 
 
