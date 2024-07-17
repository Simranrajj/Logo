import React from 'react';

const Logo = () => {
  return (
    <svg width="200" height="200" viewBox="0 0 200 200" xmlns="(link unavailable)">
      <rect x="50" y="0" width="100" height="100" fill="#8BC34A" transform="rotate(45 100 100)" />
      <rect x="50" y="100" width="100" height="100" fill="#00BCD4" transform="rotate(45 100 100)" />
      <rect x="0" y="50" width="100" height="100" fill="#FF9800" transform="rotate(45 100 100)" />
      <rect x="100" y="50" width="100" height="100" fill="#E91E63" transform="rotate(45 100 100)" />
      <text x="50%" y="55%" textAnchor="middle" fill="white" fontSize="20" fontFamily="Arial">HTML&CSS</text>
      <text x="50%" y="65%" textAnchor="middle" fill="white" fontSize="10" fontFamily="Arial">design and build websites</text>
    </svg>
  );
};

export default Logo;