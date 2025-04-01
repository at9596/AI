#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests

def fetch_github_profile(username):
    url = f"https://api.github.com/users/{username}/repos?sort=updated"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for {username}")
        return None


# In[3]:


username = 'at9596'
profile_data = fetch_github_profile(username)
profile_data


# In[5]:


import requests

def fetch_github_profile(username):
    url = f"https://api.github.com/users/{username}/repos?sort=updated"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for {username}")
        return None

# Set username and call the function
username = 'at9596'
profile_data = fetch_github_profile(username)

# Display the profile data
# profile_data


# In[6]:


def display_profile_data(profile_data):
    """
    Display GitHub profile information.
    """
    if profile_data:
        print(f"Username: {profile_data['login']}")
        print(f"Name: {profile_data['name']}")
        print(f"Bio: {profile_data.get('bio', 'No bio available')}")
        print(f"Followers: {profile_data['followers']}")
        print(f"Following: {profile_data['following']}")
        print(f"Public Repos: {profile_data['public_repos']}")
        print(f"Public Gists: {profile_data['public_gists']}")
        print(f"Profile URL: {profile_data['html_url']}")
    else:
        print("No profile data available.")

# Display the profile data for the user
display_profile_data(profile_data)


# In[8]:


import requests

def fetch_github_profile(username):
    url = f"https://api.github.com/users/{username}/repos?sort=updated"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for {username}")
        return None

# Set username and call the function
username = 'at9596'
profile_data = fetch_github_profile(username)

# Display the profile data
# profile_data
def display_profile_data(profile_data):
    """
    Display GitHub profile information.
    """
    if profile_data:
        print(f"Username: {profile_data['login']}")
        print(f"Name: {profile_data['name']}")
        print(f"Bio: {profile_data.get('bio', 'No bio available')}")
        print(f"Followers: {profile_data['followers']}")
        print(f"Following: {profile_data['following']}")
        print(f"Public Repos: {profile_data['public_repos']}")
        print(f"Public Gists: {profile_data['public_gists']}")
        print(f"Profile URL: {profile_data['html_url']}")
    else:
        print("No profile data available.")

# Display the profile data for the user
display_profile_data(profile_data)


# In[9]:


import requests

def fetch_github_profile(username):
    # Fetch the profile data from the correct GitHub API endpoint
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Return the profile data as a dictionary
    else:
        print(f"Error: Unable to fetch data for {username}")
        return None

def display_profile_data(profile_data):
    """
    Display GitHub profile data for the user.
    """
    if profile_data:
        # Display user profile data
        print(f"Username: {profile_data['login']}")
        print(f"Name: {profile_data['name']}")
        print(f"Bio: {profile_data.get('bio', 'No bio available')}")
        print(f"Public Repos: {profile_data['public_repos']}")
        print(f"Followers: {profile_data['followers']}")
        print(f"Following: {profile_data['following']}")
        print(f"Profile URL: {profile_data['html_url']}")
    else:
        print("No profile data to display.")

# Example usage
username = 'at9596'
profile_data = fetch_github_profile(username)

# Display the profile data for the user
display_profile_data(profile_data)


# In[ ]:




