###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2021, John McNamara, jmcnamara@cpan.org
#

import unittest
from io import StringIO
from ..helperfunctions import _xml_to_list
from ...drawing import Drawing


class TestAssembleDrawing(unittest.TestCase):
    """
    Test assembling a complete Drawing file.

    """
    def test_assemble_xml_file(self):
        """Test writing a drawing with no cell data."""
        self.maxDiff = None

        fh = StringIO()
        drawing = Drawing()
        drawing._set_filehandle(fh)

        dimensions = [2, 1, 0, 0, 3, 6, 533257, 190357, 1219200, 190500, 0, 0]
        drawing_object = drawing._add_drawing_object()
        drawing_object['type'] = 2
        drawing_object['dimensions'] = dimensions
        drawing_object['width'] = 1142857
        drawing_object['height'] = 1142857
        drawing_object['description'] = 'republic.png'
        drawing_object['shape'] = None
        drawing_object['anchor'] = 2
        drawing_object['rel_index'] = 1
        drawing_object['url_rel_index'] = 0
        drawing_object['tip'] = None

        drawing.embedded = 1

        drawing._assemble_xml_file()

        exp = _xml_to_list("""
                <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                <xdr:wsDr xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                  <xdr:twoCellAnchor editAs="oneCell">
                    <xdr:from>
                      <xdr:col>2</xdr:col>
                      <xdr:colOff>0</xdr:colOff>
                      <xdr:row>1</xdr:row>
                      <xdr:rowOff>0</xdr:rowOff>
                    </xdr:from>
                    <xdr:to>
                      <xdr:col>3</xdr:col>
                      <xdr:colOff>533257</xdr:colOff>
                      <xdr:row>6</xdr:row>
                      <xdr:rowOff>190357</xdr:rowOff>
                    </xdr:to>
                    <xdr:pic>
                      <xdr:nvPicPr>
                        <xdr:cNvPr id="2" name="Picture 1" descr="republic.png"/>
                        <xdr:cNvPicPr>
                          <a:picLocks noChangeAspect="1"/>
                        </xdr:cNvPicPr>
                      </xdr:nvPicPr>
                      <xdr:blipFill>
                        <a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="rId1"/>
                        <a:stretch>
                          <a:fillRect/>
                        </a:stretch>
                      </xdr:blipFill>
                      <xdr:spPr>
                        <a:xfrm>
                          <a:off x="1219200" y="190500"/>
                          <a:ext cx="1142857" cy="1142857"/>
                        </a:xfrm>
                        <a:prstGeom prst="rect">
                          <a:avLst/>
                        </a:prstGeom>
                      </xdr:spPr>
                    </xdr:pic>
                    <xdr:clientData/>
                  </xdr:twoCellAnchor>
                </xdr:wsDr>
                """)

        got = _xml_to_list(fh.getvalue())

        self.assertEqual(got, exp)

    def test_assemble_xml_file_with_url(self):
        """Test writing a drawing with no cell data."""
        self.maxDiff = None

        fh = StringIO()
        drawing = Drawing()
        drawing._set_filehandle(fh)

        drawing = Drawing()
        drawing._set_filehandle(fh)

        dimensions = [2, 1, 0, 0, 3, 6, 533257, 190357, 1219200, 190500, 0, 0]
        drawing_object = drawing._add_drawing_object()
        drawing_object['type'] = 2
        drawing_object['dimensions'] = dimensions
        drawing_object['width'] = 1142857
        drawing_object['height'] = 1142857
        drawing_object['description'] = 'republic.png'
        drawing_object['shape'] = None
        drawing_object['anchor'] = 2
        drawing_object['rel_index'] = 2
        drawing_object['url_rel_index'] = 1
        drawing_object['tip'] = 'this is a tooltip'

        drawing.embedded = 1

        drawing._assemble_xml_file()

        exp = _xml_to_list("""
                <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                <xdr:wsDr xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                  <xdr:twoCellAnchor editAs="oneCell">
                    <xdr:from>
                      <xdr:col>2</xdr:col>
                      <xdr:colOff>0</xdr:colOff>
                      <xdr:row>1</xdr:row>
                      <xdr:rowOff>0</xdr:rowOff>
                    </xdr:from>
                    <xdr:to>
                      <xdr:col>3</xdr:col>
                      <xdr:colOff>533257</xdr:colOff>
                      <xdr:row>6</xdr:row>
                      <xdr:rowOff>190357</xdr:rowOff>
                    </xdr:to>
                    <xdr:pic>
                    <xdr:nvPicPr>
                        <xdr:cNvPr id="2" name="Picture 1" descr="republic.png">
                          <a:hlinkClick xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:id="rId1" tooltip="this is a tooltip"/>
                        </xdr:cNvPr>
                        <xdr:cNvPicPr>
                            <a:picLocks noChangeAspect="1"/>
                        </xdr:cNvPicPr>
                    </xdr:nvPicPr>
                    <xdr:blipFill>
                        <a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="rId2"/>
                        <a:stretch>
                            <a:fillRect/>
                        </a:stretch>
                    </xdr:blipFill>
                      <xdr:spPr>
                        <a:xfrm>
                          <a:off x="1219200" y="190500"/>
                          <a:ext cx="1142857" cy="1142857"/>
                        </a:xfrm>
                        <a:prstGeom prst="rect">
                          <a:avLst/>
                        </a:prstGeom>
                      </xdr:spPr>
                    </xdr:pic>
                    <xdr:clientData/>
                  </xdr:twoCellAnchor>
                </xdr:wsDr>
                """)

        got = _xml_to_list(fh.getvalue())

        self.assertEqual(got, exp)
