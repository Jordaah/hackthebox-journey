export const post = async (url, data) => {
    return await fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "X-SPACE-NO-CSRF": "1",
            "Content-Type": "application/json",
        },
        credentials: "include",
    })
}

export const postForm = async (url, formData) => {
    return await fetch(url, {
        method: "POST",
        body: formData,
        headers: {
            "X-SPACE-NO-CSRF": "1",
        },
        credentials: "include",
    })
}

export const get = async (url) => {
    return await fetch(url, {
        credentials: "include",
    })
}