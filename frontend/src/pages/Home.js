import SearchBarComponent from "../components/Search";
export default function Home() {
    return (
            <div
            style={{
                display: "flex",
                alignSelf: "center",
                justifyContent: "center",
                flexDirection: "column",
                padding: 20,
                margin: "auto"
              }}>
                <p> Search </p>
                <SearchBarComponent/>
            </div>
            
    );
  }