import { useState } from "react";
import Row from "react-bootstrap/Row";
import "./App.css";
import Product from "./Components/Product";
import Container from "react-bootstrap/Container";
import { getAllProducts } from "./utils/dataExtractor";

function App() {
  const productos = getAllProducts();
  return (
    <>
      <Container>
        <Row mb={4}>
          {productos.map((producto, index) => (
            <Product
              key={index}
              name={producto.name}
              url={producto.url}
              tienda={producto.tienda}
              price={producto.price}
              discount={producto.discount}
            />
          ))}
        </Row>
      </Container>
    </>
  );
}

export default App;
