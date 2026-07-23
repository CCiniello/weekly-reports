export default async (request, context) => {
  const USER = "team";
  const PASS = "IGWeeklyReports";

  const auth = request.headers.get("authorization");
  if (auth) {
    const [scheme, encoded] = auth.split(" ");
    if (scheme === "Basic") {
      const decoded = atob(encoded);
      const i = decoded.indexOf(":");
      if (decoded.slice(0, i) === USER && decoded.slice(i + 1) === PASS) {
        return context.next();
      }
    }
  }
  return new Response("Authentication required.", {
    status: 401,
    headers: { "WWW-Authenticate": 'Basic realm="Weekly Reports"' },
  });
};

export const config = { path: "/*" };
