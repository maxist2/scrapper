import productos from "../data/data_base.json";

export interface Product {
  name: string;
  price: number;
  discount?: number;
  tienda: string;
  url: string;
}

export const getAllProducts = (): Product[] => {
  const allProducts: Product[] = [];
  for (const storeKey in productos) {
    if (Object.prototype.hasOwnProperty.call(productos, storeKey)) {
      const storeProducts = productos[storeKey];
      storeProducts.forEach((product: any) => {
        allProducts.push({
          name: product.nombre,
          price: product.precio,
          discount: product.descuento,
          tienda: product.tienda,
          url: product.url,
        });
      });
    }
  }
  return allProducts;
};