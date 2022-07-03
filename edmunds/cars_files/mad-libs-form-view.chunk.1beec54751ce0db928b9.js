(window.webpackJsonp=window.webpackJsonp||[]).push([["mad-libs-form-view"],{"./site-modules/shared/components/lead-form/unified-lead-form/views/form-view/mad-libs/mad-libs-form-view.jsx":function(e,a,l){"use strict";l.r(a),l.d(a,"MadLibsFormViewUI",function(){return B}),l.d(a,"MadLibsFormView",function(){return F});var r=l("../node_modules/@babel/runtime/helpers/esm/objectSpread.js"),s=l("../node_modules/react/index.js"),m=l.n(s),n=l("../node_modules/prop-types/index.js"),t=l.n(n),i=l("../node_modules/classnames/index.js"),d=l.n(i),o=l("../node_modules/reactstrap/lib/Row.js"),c=l.n(o),p=l("../node_modules/reactstrap/lib/Col.js"),u=l.n(p),f=l("./site-modules/shared/components/lead-form/utils/utils.js"),b=l("./site-modules/shared/components/lead-form/lead-form-prop-types/lead-form-prop-types.jsx"),N=l("./site-modules/shared/components/lead-form/unified-lead-form/views/form-view-decorator.jsx"),h=l("../node_modules/reactstrap/lib/FormGroup.js"),E=l.n(h),v=l("./site-modules/shared/components/form-field/form-field.jsx"),x=l("../node_modules/reactstrap/lib/Button.js"),j=l.n(x),y=l("./site-modules/shared/components/form-field-mask/form-field-mask.jsx"),w=l("./site-modules/shared/constants/lead-form/validation.js"),_=l("./site-modules/shared/components/lead-form/unified-lead-form/components/privacy-note/privacy-note.jsx"),g=l("./site-modules/shared/utils/inventory-utils/append-trademark-character.js");const k="w-100 mb-0",C="text-gray-darker mb-0",V="xsmall text-danger";class B extends s.Component{render(){const e=this.props,a=e.fieldRef,l=e.validationErrors,r=e.validate,n=e.year,t=e.make,i=e.model,o=e.customConfig,p=o.submitButtonText,b=o.tcpaParentDealershipName,N=e.profile,h=!("firstName"in l),x=!("lastName"in l),B=!("email"in l),F=!("phone"in l),O=Object(f.q)(N),q=O.firstName,L=O.lastName,P=O.email,T=O.phoneNumber,$=Object(g.a)({make:t,str:`${n} ${t} ${i}`});return m.a.createElement(s.Fragment,null,m.a.createElement(c.a,{className:"mt-1_5"},m.a.createElement(u.a,{xs:12},m.a.createElement("div",{className:d()("user-info mb-0_5 rounded")},m.a.createElement("div",{className:"d-inline-flex"},"Hi, my name is"),m.a.createElement(E.a,{className:"d-inline-flex mx-0_5 mb-1 form-inline"},m.a.createElement("div",null,m.a.createElement(v.a,{id:"lead-form-embeded-fname",name:"firstName",placeholder:"first name",ref:a,"aria-required":!0,"aria-invalid":!h,"aria-describedby":"error-firstName","aria-label":"first name",isValid:h,labelClassName:C,maxLength:60,onBlur:r,defaultValue:q,className:"mb-0"}),m.a.createElement("span",{id:"error-firstName",className:V},l.firstName))),m.a.createElement(E.a,{className:"d-inline-flex mr-0_5 mr-md-1 mb-1 form-inline"},m.a.createElement("div",null,m.a.createElement(v.a,{id:"lead-form-embeded-lname",name:"lastName",placeholder:"last name",ref:a,"aria-required":!0,"aria-invalid":!x,"aria-describedby":"error-lastName","aria-label":"last name",isValid:x,maxLength:60,onBlur:r,defaultValue:L,className:"mb-0"}),m.a.createElement("span",{id:"error-lastName",className:V},l.lastName))),m.a.createElement("div",{className:"d-inline mb-1"},"and I'm interested in this ",$,". You can contact me at\xa0"),m.a.createElement(E.a,{className:"d-inline-flex mt-1"},m.a.createElement("div",{className:"user-info-email"},m.a.createElement(v.a,{id:"lead-form-embeded-email",name:"email",placeholder:"email address",ref:a,"aria-required":!0,"aria-invalid":!B,"aria-describedby":"error-email","aria-label":"email address",isValid:B,type:"email",className:k,labelClassName:C,onBlur:r,defaultValue:P}),m.a.createElement("span",{id:"error-email",className:V},l.email))),m.a.createElement("div",{className:"d-inline-flex mx-0_5 mb-1"},"and"),m.a.createElement(E.a,{className:"d-inline-flex form-inline"},m.a.createElement("div",null,m.a.createElement(y.a,{id:"lead-form-embeded-phone",name:"phone",placeholder:"phone number",ref:a,"aria-required":!0,"aria-invalid":!F,"aria-describedby":"error-phone","aria-label":"phone number",isValid:F,type:"tel",mask:w.a,className:k,labelClassName:C,onBlur:r,defaultValue:T}),m.a.createElement("span",{id:"error-phone",className:V},l.phone))),m.a.createElement("span",null,". Thank you!"),m.a.createElement("div",{className:"mt-1"},m.a.createElement(j.a,{type:"submit",color:"outline-primary",className:"submit-button btn-lg px-0_75 py-0_5"},m.a.createElement("i",{className:"spinner icon-spinner8 mr-0_25"}),m.a.createElement("span",null,p)),m.a.createElement("div",{className:"mt-1"},m.a.createElement(_.a,{tcpaParentDealershipName:b,classNames:"mb-1"})))))))}}B.propTypes=Object(r.a)({},b.h,{customConfig:b.p.leadFormConfig,profile:t.a.shape({})}),B.defaultProps=Object(r.a)({},b.g,{customConfig:Object(r.a)({},b.o.leadFormConfig),profile:{}});const F=Object(N.a)(B)}}]);
//# sourceMappingURL=mad-libs-form-view.chunk.88ffc8c95bbbcc31a59d.js.map