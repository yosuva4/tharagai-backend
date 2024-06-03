const add_varient = (table) => {
  const row = $(table).closest("tr");
  const weight = row.find("input:eq(0)");
  const price = row.find("input:eq(1)");

  row.find("input:eq(0)").next("span").hide();
  row.find("input:eq(1)").next("span").hide();

  let check = true;
  if (weight.val() == "") {
    check = false;
    row.find("input:eq(0)").next("span").show();
  }
  if (price.val() == "") {
    check = false;
    row.find("input:eq(1)").next("span").show();
  }

  if (check) {
    const table = $("#variation_table");
    weight.prop("disabled", true);
    price.prop("disabled", true);

    const tr = `
    <tr>
        <td>
        <input
            type="text"
            class="p-2 border outline-none rounded"
            style="width: 100%"
            placeholder="weight"
            name="weight"
        />
        <span class="text-red-500 hidden">Fill weight</span>
        </td>
        <td>
        <input
            type="number"
            class="p-2 border outline-none rounded"
            style="width: 100%"
            placeholder="price"
            name="price"
        />
        <span class="text-red-500 hidden">Fill price</span>
        </td>
        <td>
        <button
            type="button"
            class="bg-secondry p-2 px-6 rounded success-hover"
            onclick="add_product(this)"
            style="width: 100%"
        >
            Add
        </button>
        </td>
    </tr>
    `;

    table.append(tr);
  }
};

const add_benifit = (table_tr, table_set, placeholder) => {
  const row = $(table_tr).closest("tr");
  const benifit_input = row.find("input:eq(0)");

  row.find("input:eq(0)").next("span").hide();

  let check = true;
  if (benifit_input.val() == "") {
    check = false;
    row.find("input:eq(0)").next("span").show();
  }

  if (check) {
    const table = $(`${table_set}`);
    benifit_input.prop("disabled", true);

    const tr = `
    <tr>
        <td>
        <input
            type="text"
            class="p-2 border outline-none rounded"
            style="width: 100%"
            placeholder="${placeholder}"
        />
        <span class="text-red-500 hidden">fill the column</span>
        </td>
        <td>
        <button
            type="button"
            class="bg-secondry p-2 px-6 rounded success-hover"
            onclick="add_benifit(this)"
            style="width: 100%"
        >
            Add
        </button>
        </td>
    </tr>`;

    table.append(tr);
  }
};
