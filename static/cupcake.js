const base_url = 'http://127.0.0.1:5000/api'

async function get_cupcakes(){
    const res = await axios.get(`${base_url}/cupcakes`)
    for(let cupcakes of res.data.cupcakes){
        let result = $(render_html(cupcakes))
        $(".cupcake_list").append(result)
    }    
}

function render_html(cupcake){
    return `<br>
    <div data-cupcake-id=${cupcake.id}>
    <img src="${cupcake.image}", height="200", width="200">
    <li>Flavor: ${cupcake.flavor} </li>
    <li> Rating:  ${cupcake.rating} </li>
    <li> Size:  ${cupcake.size}</li><br>
    <button type="submit" id="delete_cupcake" data-id="${cupcake.id}" class="btn btn-outline-primary">Delete</button>
    </div>
    `
}

$('.cupcake_list').on("click","#delete_cupcake", async function(e){
    e.preventDefault()
    let cupcake = $(e.target).closest('div')
    let cupcakeId = cupcake.attr('data-cupcake-id')
    console.log(cupcakeId)
    await axios.delete(`${base_url}/cupcakes/${cupcakeId}`)
    cupcake.remove()
})


$('#cupcake_submit').on('submit', async function(e){
    e.preventDefault();
    let flavor = $('#flavor').val()
    let size = $('#size').val()
    let rating = $("#rating").val()
    let image = $('#image').val()

    const newCupcake = await axios.post(`${base_url}/cupcakes`,{
        flavor,
        rating,
        size,
        image
    });

    let cupcake = $(render_html(newCupcake.data.cupcake))
    $('.cupcake_list').append(cupcake)
    $('#cupcake_submit').trigger('reset')

})

$('.search').on("submit", async function(e){
    e.preventDefault()
    let search = $('#search_term').val()
    const res = axios.get(`${base_url}/cupcakes/search`, {params:{
        q: search }})
    console.log(res)
  })

$(get_cupcakes);