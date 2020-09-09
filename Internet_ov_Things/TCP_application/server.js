const encoder = new TextEncoder()
const decoder = new TextDecoder()

const listener = Deno.listen({ port: 3000 })

console.log('Listening on port 3000')

for await (const conn of listener) {
    const buf = new Uint8Array(1024)
    await conn.read(buf)
    console.log('Server - received:', decoder.decode(buf))

    await conn.write(encoder.encode('pong'))
    conn.close()
}