# High Level Programming Blog

I've created the High Level Programming blog to give myself a place to articulate programming concepts at a high level. By explaining programming concepts clearly in writing I will crystalize the knowledge I acquire and become a better programmer.

## Technologies Used

- **Frontend**: JavaScript/React.js
- **Backend**: Python/Django

## User Stories/React Architecture/Wireframes/Backend Models

[User Stories, React Architecture, and Wireframes](https://imgur.com/a/sUX8vR3)

### Backend Models

**Blog Post**
Title = text
Content = text
updated_at 
created_at

## Time/Priority Matrix

### Backend

| Component | Priority | Estimated Time | Actual Time |
| --- | :---: |  :---: | :---: |
| Python/Django database set up | H | 1hr | 0.5hr |
| Backend file structure | H | 1hr | 0.5 |
| settings, urls, models, serializers | H | 2hr | 3hr |
| views (full CRUD) test in postman | H | 2hr | 2hr |
| create superuser account, test | H | 1hr | 0.25 |
| research and implement summernote | H | 3hr | 1hr |
| Deployment | H | 3hr | 5hr |
| Total | H | 13hr | 12.25hr |

### Frontend

| Component | Priority | Estimated Time | Actual Time |
| --- | :---: |  :---: | :---: |
| Set up React App | H | 1hr | 0.5hr |
| Set up file structure | H | 1hr | 0.5hr |
| App Component | H | 1hr | 1hr |
| Nav component | H | 1hr | 0.5hr |
| Intro component | H | 1hr | 0.25hr |
| Blog List component | H | 1hr | 3hr |
| Blog List connectivity to backend | H | 3hr | 1hr |
| Blog Entry component | H | 1hr | 1hr |
| Blog Entry connectivity to backend | H | 3hr | 1hr |
| Styling | H | 3hr | TBA |
| Blog Entry component | H | 1hr | 2hr |
| Deployment | H | 2hr | 5hr |
| Total | H | 19hr | 15.75 |

## Hurdles

The project's biggest hurdle so far has been the 'Read' button within my ```<BlogList>``` component. My BlogList component uses a ternary operator to determine when to display blog content. The conditional checks for whether the ```title``` and ```content``` state has been set. If they have, the title and content of the blog post will be displayed. Originally, if the conditional found the states to be set, I used ```<Navigate to='/content'>``` as opposed to simply mounting the ```<Blog>``` component. This worked fine for having the blog content displayed, but when I would click the homepage link, the ```title``` and ```content``` states would be cleared, but the api call to my backend, which was supposed to return a complete list of blog posts, failed. I still don't fully understand why this happened. My ternary operator seemed to fail to recognize that the state had been cleared. But having my ```<Blog>``` component mount as opposed to navigating to the unnecessary content page fixed the issue. The lesson here is obvious in hindsight: Keep it simple.

