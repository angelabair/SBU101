<?xml version='1.0' encoding='UTF-8'?>
<imagefigure xmlns="http://www.standardnine.com/s9ml" designation="{{designation}}" enumeration="{{enumeration}}">
    <title>{{title}}</title>
    <img src="../../img/.templates/placeholder.png"/>
    <caption>The Image Figure blueprint displays a photograph, illustration, or other image with a scrollable caption. Poptips can provide additional context about the image.</caption>
    <cite/>
    <type>illustration</type>
    <annotations>
        <!-- This is the first poptip-->
        <annotation>
            <orientation>taildown</orientation>
            <location x="383" y="135"/>          
            <snippet><text>This is a poptip. You can remove it in Habitat by pressing “delete” or “backspace” on your keyboard.</text></snippet>
        </annotation>
        <!-- This is the second poptip-->
        <annotation>
            <orientation>tailleft</orientation>
            <location x="849" y="587"/>
            <snippet><text>To draw leader lines, hover over the poptip, then click and drag the “+” icon at its tip.</text></snippet>
            <destinations>
                <destination x="692" y="510"/>
            </destinations>
        </annotation>
    </annotations>
</imagefigure>
