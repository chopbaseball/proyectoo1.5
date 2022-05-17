

function eliminar(codigo){
  Swal.fire({
    title: 'Esta Seguro?',
    text: "Esta acción no se podra revertir!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Producto Eliminado!',
        'El producto a sido eliminado correctamente.',
        'success'
      ).then(function() {
        window.location.href="/eliminar/"+codigo
      })
    }
  })

}



function pago(){
  Swal.fire({
    title: 'Esta Seguro?',
    text: "Esta acción no se podra revertir!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Pagar!'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Pago Completado!',
        'Se a recibido la orden correctamente.',
        'success'
      )
      carrito = Carrito.objects.all()
      carrito.delete()
    }
  })
}


function eliminarCliente (codigo){
  Swal.fire({
    title: 'Esta Seguro?',
    text: "Esta acción no se podra revertir!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Cliente Eliminado!',
          'El cliente a sido eliminado correctamente.',
          'success'
        ).then(function(){
            window.location.href ="/eliminarCliente/" + codigo;
        })
      }
  })

}