// export default function App() {
//   const menuItems = [
//     { name: "Dashboard", icon: "📊" },
//     { name: "Reports", icon: "📄" },
//     { name: "Users", icon: "👥" },
//     { name: "Settings", icon: "⚙️" },
//     { name: "Notifications", icon: "🔔" },
//     { name: "Files", icon: "📁" },
//   ];

//   return (
//     <div className="min-h-screen bg-gray-100">
//       {/* NAVBAR */}
//       <nav className="bg-white shadow-md px-6 py-4 flex justify-between items-center">
//         <h1 className="text-2xl font-bold text-gray-800">MyApp</h1>

//         <ul className="flex gap-6 text-gray-700 font-medium">
//           <li className="hover:text-blue-600 cursor-pointer">Home</li>
//           <li className="hover:text-blue-600 cursor-pointer">About</li>
//           <li className="hover:text-blue-600 cursor-pointer">Contact</li>
//         </ul>
//       </nav>

//       {/* GRID MENU */}
//       <div className="p-8 max-w-6xl mx-auto">
//         <h2 className="text-xl font-semibold text-gray-800 mb-6">
//           Quick Menu
//         </h2>

//         <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
//           {menuItems.map((item) => (
//             <div
//               key={item.name}
//               className="bg-white p-6 rounded-xl shadow-md hover:shadow-lg cursor-pointer transition flex flex-col items-center justify-center"
//             >
//               <span className="text-5xl mb-3">{item.icon}</span>
//               <h3 className="text-lg font-semibold text-gray-700">{item.name}</h3>
//             </div>
//           ))}
//         </div>
//       </div>
//     </div>
//   );
// }

import { useEffect, useState, type JSX } from "react";
import axios, { type AxiosResponse } from "axios";

// Types
type Product = {
  id: number;
  name: string;
  description: string;
  price: number;
  image?: string;
  category: number;
  center?: number;
  merchant?: number;
};

type Category = {
  id: number;
  name: string;
  description?: string;
  products: Product[];
};

export default function Menu(): JSX.Element {
  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCategories = async (): Promise<void> => {
      try {
        // Fetch categories
        const categoriesResponse: AxiosResponse<Category[]> = await axios.get(
          "http://127.0.0.1:8000/api/products/categories/",
          { withCredentials: true }
        );

        // Fetch products for each category
        const categoriesWithProducts: Category[] = await Promise.all(
          categoriesResponse.data.map(async (category: Category) => {
            const productsResponse: AxiosResponse<Product[]> = await axios.get(
              `http://127.0.0.1:8000/api/products/products/?category=${category.id}`,
              { withCredentials: true }
            );
            return { ...category, products: productsResponse.data };
          })
        );

        setCategories(categoriesWithProducts);
      } catch (err: unknown) {
        console.error(err);
        setError("Failed to fetch menu data.");
      } finally {
        setLoading(false);
      }
    };

    fetchCategories();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen text-xl">
        Loading menu...
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex justify-center items-center min-h-screen text-red-600 text-xl">
        {error}
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-200 p-8">
      <h1 className="text-4xl font-extrabold text-center text-gray-800 mb-10 drop-shadow-sm">
        ✨ Coffee & Tea Menu
      </h1>

      {categories.map((category: Category) => (
        <div key={category.id} className="mb-12">
          <h2 className="text-2xl font-bold mb-6 text-gray-700">{category.name}</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {category.products.map((product: Product) => (
              <div
                key={product.id}
                className="bg-white rounded-2xl p-6 shadow-md hover:shadow-xl transition flex flex-col items-center"
              >
                {product.image && (
                  <img
                    src={product.image}
                    alt={product.name}
                    className="h-32 w-32 object-cover rounded-lg mb-4"
                  />
                )}
                <h3 className="text-xl font-semibold">{product.name}</h3>
                <p className="text-gray-600 text-center">{product.description}</p>
                <p className="text-lg font-bold mt-2">${product.price}</p>
              </div>
            ))}
          </div>
        </div>
      ))}

      <p className="text-center text-sm text-gray-600 mt-12">
        Coffee & Tea Service — Powered by Django + React
      </p>
    </div>
  );
}
