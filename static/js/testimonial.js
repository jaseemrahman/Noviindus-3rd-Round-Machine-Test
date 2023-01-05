$(function () {
      var loadForm =function () {
        console.log('delete')
      var btn = $(this);
      $.ajax({
        
        url:btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modaldemo5").modal("show");
        },
        success: function (data) {
          $("#modal-menu .modal-content").html(data.html_form);
        }
      });
      };


      //   var saveForm = function () {
      //   var form = $(this);
      //   $.ajax({
      //     url: form.attr("action"),
      //     data: form.serialize(),
      //     type: form.attr("method"),
      //     dataType: 'json',
      //     success: function (data) {
      //       if (data.form_is_valid) {
      //           $("#menu-table tbody").html(data.html_product_list);  // <-- Replace the table body
      //           $("#modal-menu").modal("hide");
      //       }
      //       else {
      //         $("#modal-menu .modal-content").html(data.html_form);
      //       }
      //     }
      //   });
      //   return false;
      // };


  // Delete item
  $("#table5").on("click", ".js-delete-testimonial", loadForm);
  // $("#modal-menu").on("submit", ".js-product-delete-form", saveForm);
});
  
