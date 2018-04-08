import o from "mithril";
import {required} from "validatex";
import {UI} from "./base";


export class Navbar extends UI {

    view ({attrs, children}) {
        return o("div",
                 {"class": "navbar navbar-expand-lg navbar-light bg-light"},
                 children);
    }
}


export class Layout extends UI {

    view ({children}) {
        return o(
            "div", o(Navbar), children
        );
    }
}
