// import React from "react";

// export default function Menu() {
//   const items = [
//     { name: "Admin Panel", url: "/admin/", emoji: "🛠" },

//     // CORE
//     { name: "Companies", url: "/core/companies/", emoji: "🏭" },
//     { name: "Factories", url: "/core/factories/", emoji: "🏢" },
//     { name: "Admin Regions", url: "/core/admin-regions/", emoji: "🌍" },
//     { name: "Cities", url: "/core/cities/", emoji: "🏘️" },

//     // SALES
//     { name: "Sales Orders", url: "/sales/orders/", emoji: "🧾" },
//     { name: "Order Items", url: "/sales/order-items/", emoji: "📦" },

//     // INVENTORY
//     { name: "Warehouses", url: "/inventory/warehouses/", emoji: "🏚️" },
//     { name: "Products", url: "/inventory/products/", emoji: "🛒" },
//     { name: "Stocks", url: "/inventory/stocks/", emoji: "📊" },

//     // USERS
//     { name: "Users", url: "/users/users/", emoji: "👤" },
//   ];

//   return (
//     <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-200 p-8 flex justify-center">
//       <div className="w-full max-w-5xl">
//         <h1 className="text-4xl font-extrabold text-center text-gray-800 mb-10 drop-shadow-sm">
//           ✨ Milki ERP Menu
//         </h1>

//         <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
//           {items.map((item, index) => (
//             <a
//               key={index}
//               href={item.url}
//               className="
//                 bg-white/80 backdrop-blur-lg 
//                 border border-gray-200 
//                 rounded-2xl p-8 
//                 shadow-md 
//                 hover:shadow-xl 
//                 hover:-translate-y-1 
//                 transition 
//                 text-center 
//                 flex flex-col items-center 
//               "
//             >
//               <span className="text-5xl mb-4">{item.emoji}</span>
//               <h2 className="text-xl font-semibold text-gray-800">{item.name}</h2>
//             </a>
//           ))}
//         </div>

//         <p className="text-center text-sm text-gray-600 mt-12">
//           Milki ERP — Powered by Django + React
//         </p>
//       </div>
//     </div>
//   );
// }

import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Menu() {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMenu = async () => {
      try {
        // Fetch categories
        const categoriesRes = await axios.get(
          "http://127.0.0.1:8000/api/products/categories/"
        );

        // Fetch products
        const productsRes = await axios.get(
          "http://127.0.0.1:8000/api/products/products/"
        );

        // Group products by category
        const grouped = categoriesRes.data.map((category) => ({
          ...category,
          products: productsRes.data.filter(
            (p) => p.category === category.id
          ),
        }));

        setCategories(grouped);
      } catch (err) {
        console.error("Error fetching menu:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchMenu();
  }, []);

  if (loading) return <p className="text-center mt-10">Loading menu...</p>;

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-4xl font-bold text-center mb-10">☕ Coffee & Tea Menu</h1>
      {categories.map((category) => (
        <div key={category.id} className="mb-12">
          <h2 className="text-2xl font-semibold mb-4">{category.name}</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {category.products.map((product) => (
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
    </div>
  );
}
