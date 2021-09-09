import axios from "axios";
import { error_codes } from "./errors"

axios.defaults.headers["Content-Type"] = "application/json"
axios.defaults.baseURL = process.env.REACT_APP_API_URL;


export default axios;
