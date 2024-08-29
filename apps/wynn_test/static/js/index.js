"use strict";

// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};


app.data = {    
    data: function() {
        return {
            // Complete as you see fit.
            my_value: 1, // This is an example.
            sample_data: null,
            head: null,
            username: null,
            online: null,
            hours: 0.0,
            raids: 0,
            players: [
                {username: "vic", hours: 10, raids: 20},
                {username: "vicc", hours: 10, raids: 21},
                {username: "viccc", hours: 10, raids: 22},
                {username: "vicccc", hours: 10, raids: 23},
                {username: "viccccc", hours: 10, raids: 24},
            ],
        };
    },
    methods: {
        // Complete as you see fit.
        my_function: function() {
            // This is an example.
            this.my_value += 1;
        },
        my_test: function() {
            // do api call
            self = this
            console.log("making api call")
            axios.get(wynn_call_url).then(function (r) {
                self.sample_data = r.data
                // self.raids = r.data.globalData.raids.total
                console.log("data is: ", self.sample_data)
                // console.log("testing, name is: ", self.sample_data.data.username)
                // console.log("testing, guild is: ", self.sample_data.data.guild.name, self.sample_data.data.guild.prefix)
            });
        },
    }
};

app.vue = Vue.createApp(app.data).mount("#app");

app.load_data = function () {
    axios.get(my_callback_url).then(function (r) {
        app.vue.my_value = r.data.my_value;
    });
    axios.get(get_head_url).then(function (r) {
        app.vue.head = r.data.head
    })
    axios.get(wynn_call_url).then(function (r) {
        app.vue.sample_data = r.data.player
        app.vue.username = r.data.player.username
        app.vue.online = r.data.player.online
        app.vue.hours = r.data.player.playtime
        app.vue.raids = r.data.player.globalData.raids.total
    });
}

app.load_data();

