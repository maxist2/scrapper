import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";

interface Props {
  name: string;
  price: number;
  discount?: number;
  tienda: string;
  url: string;
}

const Product = ({ name, price, discount, tienda, url }: Props) => {
  return (
    <Col>
      <Card style={{ width: "18rem" }}>
        <Card.Body>
          <Card.Title>{name}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted">
            {`$${price} ${discount ? `($${discount})` : ""}`}
          </Card.Subtitle>
          <Card.Text>
            {` 
          tienda:${tienda}
          `}
            <hr />
            <h6>
              link:<Card.Link href={url}>{url}</Card.Link>
            </h6>
          </Card.Text>
        </Card.Body>
      </Card>
    </Col>
  );
};

export default Product;
