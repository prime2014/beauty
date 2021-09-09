import React, { Component } from "react";
import { blogsAPI } from "../../services/blogs/blogs.service";



class Home extends Component {
    constructor(props){
        super(props);
        this.state = {
            blogs: []
        }
    }

    componentDidMount(){
        blogsAPI.fetchBlogs().then(resp=>{
            this.setState({
                blogs: resp
            })
        })
    }

    render(){
        let { blogs } = this.state;
        return(
            <div>
                <h1 className="blog-header">Blogs</h1>

                <main>
                    {blogs.map(blog=>{
                        return(
                            <div className="blog-card" key={blog.pk}>
                              <h4 className="article-title">{blog.title}</h4>
                              <span>written by: {blog.author.first_name} {blog.author.last_name}</span>
                              <p className="article">{blog.article.substring(0, 120)}...</p>
                            </div>
                        )
                    })}
                </main>
            </div>
        )
    }
}


export default Home;
