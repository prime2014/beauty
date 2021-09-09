import axios  from "../axios.config";



const fetchBlogs = async () => {
    try {
        let blog = null;
        let response = await axios.get("/blogs/api/v1/blogs/")
        if (response) blog = response.data;
        console.log(response);
        return blog
    } catch(error){
        return error.response.data;
    }
}


export const blogsAPI = {
    fetchBlogs
}
