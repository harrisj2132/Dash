$(function () {
    var tableDataNested = [
        {name:"Oli Bob", location:"United Kingdom", gender:"male", col:"red", dob:"14/04/1984", _children:[
            {name:"Oli Bob", location:"Germany", gender:"female", col:"blue", dob:"14/05/1982"},
            {name:"Oli Bob", location:"France", gender:"female", col:"green", dob:"22/05/1982"},        
        ]},
        {name:"Jamie Newhart", location:"India", gender:"male", col:"green", dob:"14/05/1985"},
        {name:"Gemma Jane", location:"China", gender:"female", col:"red", dob:"22/05/1982", _children:[
            {name:"Gemma Jane", location:"South Korea", gender:"female", col:"maroon", dob:"11/11/1970"},
        ]},
        {name:"James Newman", location:"Japan", gender:"male", col:"red", dob:"22/03/1998"},
        {name:"Brendon Philips", location:"USA", gender:"male", col:"orange", dob:"01/08/1980", _children:[
          {name:"", location:"Canada", gender:"female", col:"yellow", dob:"31/01/1999"},
          {name:"", location:"Russia", gender:"male", col:"red", dob:"12/05/1966"},
        ]},
    ];
      
      //Build Tabulator
      var table = new Tabulator("#example-table", {
        height:"311px",
        data:tableDataNested,
        dataTree:true,
        headerSort: true,
        movableColumns: true,
        dataTreeStartExpanded:true,
        columns:[
          { formatter: "rowSelection", field: 'IsSelected', titleFormatter: "rowSelection", hozAlign: "center", headerSort: false, cellClick: function (e, cell) { console.log(cell); cell.getRow().toggleSelect(); }, download: false },
        {title:"Name", field:"name", headerFilter: "input", width:200, responsive:0}, //never hide this column
        {title:"Location", field:"location", headerFilter: "input", editor: "input", validator: ["required"], width:150},
        {title:"Gender", field:"gender", headerFilter: "input", editor: "input", validator: ["required"], width:150, responsive:2}, //hide this column first
        {title:"Favourite Color", field:"col", headerFilter: "input", editor: "input", width:150},
        {title:"Date Of Birth", field:"dob", hozAlign:"center",  sorter:"date", width:150},
        ],
    });
    });
    