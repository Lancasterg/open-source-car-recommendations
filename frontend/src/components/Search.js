import { useState } from "react";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
import TextField from "@mui/material/TextField";
import axios from "axios";


export default function SearchBarComponent(props){
    const [registration, setRegistration] = useState('');


    function handleClick() {
        const config = {
                sent_registration: registration,
        };
        
        console.log(registration);
        axios.get("http://localhost:5000/motHistory/" + registration, config)
        
        .then(result => { console.log(result); return result; })
        .catch(error => { console.error(error); return Promise.reject(error); });
    }
  
    return (
      <div
        style={{
          display: "flex",
          alignSelf: "center",
          justifyContent: "center",
          flexDirection: "column",
          padding: 20
        }}>
        <form>
        <TextField
        id="search-bar"
        className="text"
        label="Registration"
        variant="outlined"
        placeholder="Registration"
        size="small"
        helperText="Please enter your registration"
        value={registration}
        onInput={ e=>setRegistration(e.target.value)}
        />
        <IconButton type="Button" aria-label="search" onClick={() => handleClick()}>
        <SearchIcon style={{ fill: "blue" }} />
      </IconButton>
    </form>
        <div style={{ padding: 3 }}></div>
      </div>
    );
  };