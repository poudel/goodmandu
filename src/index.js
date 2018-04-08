import o from "mithril";

import {
    UI,
    Layout
} from "./ui";

import "./index.scss";


class Dashboard extends UI {

    view (vnode) {
	return o(Layout, "Welcome");
    }

}


o.route.prefix("#");
o.route(document.body, "/dashboard/", {
    "/dashboard/": Dashboard
});
