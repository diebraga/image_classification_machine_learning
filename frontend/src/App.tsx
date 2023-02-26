import React, { useState } from "react";
import axios from "axios";
import "./App.css";

type ImageFile = File & {
  preview: string;
};

function App() {
  const [image, setImage] = useState<ImageFile | null>(null);
  const [imageUrl, setImageUrl] = useState<string>("");
  const [prediction, setPrediction] = useState(
    {} as { prediction: string; probability: string }
  );

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const selectedImage = e.target.files[0];
      setImage(selectedImage as ImageFile);
      const imageUrl = URL.createObjectURL(selectedImage);
      setImageUrl(imageUrl);
    }
  };

  const handleFormSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData();
    if (image) {
      formData.append("file", image);
      try {
        const response = await axios.post(
          "http://localhost:8000/predict",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
              "Access-Control-Allow-Origin": "*",
            },
          }
        );
        setPrediction(response.data);
      } catch (error) {
        console.log(error);
      }
    } else {
      setPrediction({
        prediction: "no picture was uploaded",
        probability: "",
      });
    }
  };

  const isEmpty = prediction.prediction === "no picture was uploaded";

  const isDog = prediction.prediction === "is dog";

  const resultColor = !isEmpty && isDog ? "#2678fc" : "red";
  return (
    <form className="App" onSubmit={handleFormSubmit}>
      <h1>Is it a dog?</h1>
      <div className="card">
        <div>
          <input type="file" accept="image/*" onChange={handleImageChange} />
        </div>
        <div style={{ marginTop: "1rem" }}>
          {imageUrl && <img src={imageUrl} alt="selected image" height={200} />}
        </div>

        <button type="submit">PREDIC</button>
      </div>
      <p
        style={
          isEmpty
            ? { color: "red" }
            : { color: resultColor, fontWeight: 700, fontSize: "35px" }
        }
      >
        {prediction && prediction.prediction}
      </p>
      <p className="read-the-docs">
        "By uploading a picture, this program will analyze the image and predict
        whether it contains a dog or not."
      </p>
    </form>
  );
}

export default App;
