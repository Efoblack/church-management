import React from 'react';
import Icon from "./index";


const LikeIcon = props => {
    return (
        <Icon {...props} height="24px" viewBox="0 0 24 24">
            <g>
                <rect x="0" y="0" width="24" height="24"/>
                <path
                    d="M9,10 L9,19 L10.1525987,19.3841996 C11.3761964,19.7920655 12.6575468,20 13.9473319,20 L17.5405883,20 C18.9706314,20 20.2018758,18.990621 20.4823303,17.5883484 L21.231529,13.8423552 C21.5564648,12.217676 20.5028146,10.6372006 18.8781353,10.3122648 C18.6189212,10.260422 18.353992,10.2430672 18.0902299,10.2606513 L14.5,10.5 L14.8641964,6.49383981 C14.9326895,5.74041495 14.3774427,5.07411874 13.6240179,5.00562558 C13.5827848,5.00187712 13.5414031,5 13.5,5 L13.5,5 C12.5694044,5 11.7070439,5.48826024 11.2282564,6.28623939 L9,10 Z"
                    fill="#000000"/>
                <rect fill="#000000" opacity="0.3" x="2" y="9" width="5" height="11" rx="1"/>
            </g>
        </Icon>
    )
}


export default LikeIcon;