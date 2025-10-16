# Stage 1 — Build React app
FROM node:18 AS build

WORKDIR /app

# Copy and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy source code
COPY . .

# Build React production files
RUN npm run build

# Stage 2 — Serve using Nginx
FROM nginx:1.25-alpine

# Copy built files from build stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose default Nginx port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
