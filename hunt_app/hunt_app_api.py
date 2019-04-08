const fetchCategoryByID = (categoryID) => {
  return fetch(`https://cors-anywhere.herokuapp.com/https://craigslist-django-backend.herokuapp.com/category/${categoryID}`)
    .then((response) => response.json());
}

const fetchUsers = () => {
  return fetch(`https://cors-anywhere.herokuapp.com/https://craigslist-django-backend.herokuapp.com/category/`)
    .then((response) => response.json());
}

const addCategory = (categoryObject) => {
  return fetch('https://cors-anywhere.herokuapp.com/https://craigslist-django-backend.herokuapp.com/category/', {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify(categoryObject)
  })
}

const editCategory = (categoryID, categoryObject) => {
  return fetch(`http://localhost:8000/categories/${categoryID}/`, {
    headers: {
      'Content-Type': 'application/json'
    },
    method: "PUT",
    body: JSON.stringify(categoryObject)
  })
}

const deleteCategory = (categoryID) => {
  return fetch(`http://localhost:8000/categories/${categoryID}/`, { 
    method: 'DELETE' 
  });
}

const addPost = (postObject) => {
  return fetch('https://cors-anywhere.herokuapp.com/https://craigslist-django-backend.herokuapp.com/posts/', {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify(postObject)
  })
}

const fetchPosts = () => {
  return fetch(`https://cors-anywhere.herokuapp.com/https://craigslist-django-backend.herokuapp.com/posts/`)
    .then((response) => response.json());
}

const fetchPostsByCategory = (categoryID) => {
  return fetch(`https://cors-anywhere.herokuapp.com/https://craigslist-django-backend.herokuapp.com/posts/?filter={"where":{"categoryID":"${categoryID}"}}`)
    .then((data) => data.json())
}

const editPost = (categoryID, postID, postObject) => {
  return fetch(`http://localhost:8000/categories/${categoryID}/posts/${postID}/`, {
    headers: {
      'Content-Type': 'application/json'
    },
    method: "PUT",
    body: JSON.stringify(postObject)
  })
}

const deletePost = (postID) => {
  return fetch(`http://localhost:8000/posts/${postID}/`, { 
    method: 'DELETE' 
  });
}


export default {
  fetchCategoryByID: fetchCategoryByID,
  fetchCategories: fetchCategories,
  addCategory: addCategory,
  editCategory: editCategory,
  deleteCategory: deleteCategory,
  fetchPosts: fetchPosts,
  addPost: addPost,
  fetchPostsByCategory: fetchPostsByCategory,
  editPost: editPost,
  deletePost: deletePost
}