import os
import matplotlib.pyplot as plt
import warnings


warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

 
def rbdCodeNames(df, country, outfile, imagepath):
    html_string = '''<h3>RBD Code and names </h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _1_surfaceWaterBodyNumberAndSite2016(df, country, outfile, imagepath):
    html_string = '''<h3>1. Number and size of surface water bodies </h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Country', 'Number']].plot.bar('Country', 'Number', rot=0)
        plt.title('Surface Waters bodies\nNumber')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'1.surfaceWaterBodyNumberAndSite2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'

    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _2_GroundWaterBodyCategory2016(df, country, outfile, imagepath):
    html_string = '''<h3>2. Number and size of groundwater bodies</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Country', 'Number']].plot.bar('Country', 'Number', rot=0, color="#653700")
        plt.title('Groundwater bodies\nNumber')
        plt.xlabel('')
        plt.ylabel('Total Number of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'2.GroundWaterBodyCategory2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _3_surfaceWaterBodyCategory2016(df, country, outfile, imagepath):
    html_string = '''<h3>3. Number of surface water bodies by category and type</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        categories = ["RW", "LW", "TW", "CW", "TeW"]
        for categ in categories:
            if not temp.loc[(temp['Surface Water Body Category'] == categ)].empty:
                temp1 = temp.loc[(temp['Surface Water Body Category'] == categ)]
                temp1['Wrap Values'] = temp1['Type'].str.wrap(20)
                temp1[['Wrap Values', 'Total']].plot.bar('Wrap Values', 'Total', rot=65)
                plt.title('Number of surface water bodies by category and type\n(' + categ + ')')
                plt.xlabel('')
                plt.ylabel('Total Number of\nSurface water bodies')
                plt.gcf()
                plt.draw()
                figfilename = os.path.join(imagepath, f'3.surfaceWaterBodyCategory2016{country}.png')
                plt.savefig(figfilename, bbox_inches='tight')
                plt.close()
                html_string += '<br><br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _4_SOW_SWB_SWB_swSignificantImpactType_Table2016(df, country, outfile, imagepath):
    html_string = '''<h3>4. Surface water bodies significant pressures and impacts</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp['Wrap Values'] = temp['Significant Impact Type'].str.wrap(30)
        temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'], rot=65, figsize=(12, 4))
        plt.title('Surface water bodies\nsignificant impacts')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nsurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'4.SOW_SWB_SWB_swSignificantImpactType_Table2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _4_SOW_SWB_SWB_swSignificantImpactType_Table_Other2016(df, country, outfile, imagepath):
    html_string = '''<br>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _4_SOW_SWB_SWB_swSignificant_Pressure_Type_Table2016(df, country, outfile, imagepath):
    html_string = '''<br>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _4_SOW_SWB_SWB_swSignificantPressureType_Table_Other(df, country, outfile, imagepath):
    df.dropna()
    values = df.loc[(df['Country'] == country)]
    if not values.empty:
        html_string = '''<br>'''
        html_string += values.to_html(index=False)
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _5_SOW_GWB_gwSignificantPressureType_NumberOfImpact_by_country(df, country, outfile, imagepath):
    html_string = '''<h3>5. Groundwater bodies significant pressures and impacts</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Number of Impacts', 'Area (km^2)']].plot.bar('Number of Impacts', 'Area (km^2)', rot=0, color="#653700")
        plt.title('Groundwater bodies\nNumber of impacts')
        plt.xlabel('Number of impacts')
        plt.ylabel('Total Area($km^2$)')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'5.SOW_GWB_gwSignificantPressureType_NumberOfImpact_by_country{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _5_gwSignificantImpactType2016(df, country, outfile, imagepath):
    html_string = '''<br>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 4:
            temp['Wrap Values'] = temp['Significant Impact Type'].str.wrap(25)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)', rot=0, color="#653700")

        else:
            temp['Wrap Values'] = temp['Significant Impact Type'].str.wrap(30)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                                    figsize=(12, 4), rot=80, color="#653700")

        plt.title('Groundwater bodies of\nSignificant impacts')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'5.gwSignificantImpactType2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _5_gwSignificantImpactType_Other(df, country, outfile, imagepath):
    if not df.loc[(df['Country'] == country)].empty:
        html_string = '''<br>'''
        temp = df.loc[(df['Country'] == country)]

        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 3:
            temp['Wrap Values'] = temp['Significant Impact Other'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                                    rot=0, color="#653700")
        else:
            temp['Wrap Values'] = temp['Significant Impact Other'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                                    figsize=(15, 4), rot=0, color="#653700")
        plt.title('Groundwater bodies of\nSignificant impact reported as "Other"')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'5.gwSignificantImpactType_Other{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _5_SOW_GWB_gwSignificantPressureType_OtherTable2016(df, country, outfile, imagepath):
    if not df.loc[(df['Country'] == country)].empty:
        html_string = '''<br>'''
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)

        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 4:
            temp['Wrap Values'] = temp['Significant Pressure Other'].str.wrap(25)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', y=['Area (km^2)'],
                                                                        rot=0, color="#653700")
        else:
            temp['Wrap Values'] = temp['Significant Pressure Other'].str.wrap(25)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', y=['Area (km^2)'],
                                                                        figsize=(12, 4), rot=80, color="#653700")

        plt.title('Groundwater bodies of\nSignificant pressure reported as "Other"')
        plt.xlabel('')
        plt.ylabel('total Area (km^2) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'5.SOW_GWB_gwSignificantPressureType_OtherTable2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _5_gwSignificantPressureType2016(df, country, outfile, imagepath):
    if not df.loc[(df['Country'] == country)].empty:
        html_string = '''<br>'''
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)

        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 3:
            temp['Wrap Values'] = temp['Significant Pressure Type'].str.wrap(25)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)', rot=0, color="#653700")

        else:
            temp['Wrap Values'] = temp['Significant Pressure Type'].str.wrap(30)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)', figsize=(12, 4), rot=80, color="#653700")

        plt.title('Groundwater bodies of\nSignificant pressure')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'5.gwSignificantPressureType2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _6_SWB_Chemical_exemption_type2016(df, country, outfile, imagepath):
    html_string = '''<h3>6. Surface water bodies exemptions and pressures</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Chemical Exemption Type', 'Area (km^2)']].plot.bar('Chemical Exemption Type', 'Area (km^2)',
                                                                rot=15)
        plt.title('Surface water bodies\nChemical exemption type')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'6. SWB_Chemical_exemption_type2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _6_Surface_water_bodies_Ecological_exemptions_Type2016(df, country, outfile, imagepath):
    html_string = '''<br>
            '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[(df['Country'] == country)].count()
        if Arguments['Country'] < 2:
            temp['Wrap Values'] = temp['Ecological Exemption Type'].str.wrap(25)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', 'Number', rot=0)
        else:
            temp['Wrap Values'] = temp['Ecological Exemption Type'].str.wrap(30)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', 'Number',
                                                    figsize=(15, 4), rot=15)

        plt.title('Surface water body\nEcological exemption')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'6.Surface_water_bodies_Quality_element_exemptions_Type2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _6_Surface_water_bodies_Ecological_exemptions_and_pressures2016(df, country, outfile, imagepath):
    if not df.loc[(df['Country'] == country)].empty:
        html_string = '''<br>'''
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _6_Surface_water_bodies_Quality_element_exemptions_Type2016(df, country, outfile, imagepath):
    EETGList = df['Quality Element Exemption Type Group'].unique().tolist()
    if not df.loc[(df['Country'] == country)].empty:
        html_string = '''<br>'''
        for group in EETGList:
            temp = df.loc[(df['Country'] == country) & (df['Quality Element Exemption Type Group'] == group)]
            if not temp.empty:
                html_string += temp.to_html(index=False)

                Arguments = df.loc[(df['Country'] == country) & (df['Quality Element Exemption Type Group'] == group)].count()
                if Arguments['Country'] < 2:
                    temp['Wrap Values'] = temp['Quality Element Exemption Type'].str.wrap(25)
                    temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', 'Number', rot=0)

                else:
                    temp['Wrap Values'] = temp['Quality Element Exemption Type'].str.wrap(30)
                    temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', 'Number',
                                                                        figsize=(12, 4), rot=15)

                plt.title('Surface water bodies\nQuality element exemption type')
                plt.xlabel('')
                plt.ylabel('Total Number of\nSurface water bodies')
                plt.gcf()
                plt.draw()
                figfilename = os.path.join(imagepath, f'6.Surface_water_bodies_Quality_element_exemptions_Type2016{country}.png')
                plt.savefig(figfilename, bbox_inches='tight')
                plt.close()
                html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _7_Groundwater_bodies_Chemical_Exemption_Type2016(df, country, outfile, imagepath):
    html_string = '''<h3>7. Groundwater bodies exemptions and pressures</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        try:
            temp = df.loc[(df['Country'] == country)]
            html_string += temp.to_html(index=False)
            temp['Wrap Values'] = temp['Chemical Exemption Type'].str.wrap(25)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                                    rot=45, color="#653700")
            plt.title('Groundwater bodies\nChemical exemption type')
            plt.xlabel('')
            plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
            plt.gcf()
            plt.draw()
            figfilename = os.path.join(imagepath, f'7.Groundwater_bodies_Chemical_Exemption_Type2016{country}.png')
            plt.savefig(figfilename, bbox_inches='tight')
            plt.close()
            html_string += '<br><img src = "' + figfilename + '"><br>'
        except:
            pass
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _7_Groundwater_bodies_Quantitative_Exemption_Type2016(df, country, outfile, imagepath):
    EETGList = df['Quantitative Exemption Type Group'].unique().tolist()
    EETList = df['Quantitative Exemption Type'].unique().tolist()
    html_string = '''<br>'''
    if not df.loc[(df['Country'] == country)].empty:
        for types, group in zip(EETList, EETGList):
            if not df.loc[(df['Country'] == country) & (df['Quantitative Exemption Type Group'] == group)].empty:
                temp = df.loc[(df['Country'] == country) & (df['Quantitative Exemption Type Group'] == group)]
                html_string += temp.to_html(index=False)
                temp[['Quantitative Exemption Type', 'Area (km^2)']].plot.bar('Quantitative Exemption Type',
                                                                            'Area (km^2)', rot=15, color="#653700")
                plt.title('Groundwater bodies\nQuantitative exemption type')
                plt.xlabel('')
                plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
                plt.gcf()
                plt.draw()
                figfilename = os.path.join(imagepath, f'7.Groundwater_bodies_Quantitative_Exemption_Type2016{country + group}.png')
                plt.savefig(figfilename, bbox_inches='tight')
                plt.close()
                html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _7_Groundwater_bodies_Quantitative_exemptions_and_pressures2016(df, country, outfile, imagepath):
    html_string = '''<br>'''

    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _7_gwChemicalExcemptionPressures(df, country, outfile, imagepath):
    html_string = '''<br>
    '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _8_Surface_water_bodies_Ecological_status_or_potential_group_Failing(df, country, outfile, imagepath):
    html_string = '''<h3>8. Number and percent of surface water bodies at good or high and failling to achieve good ecological status or potential</h3>
    '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Country', 'Number']].plot.bar('Country', y=['Number'], rot=0)
        plt.title('Surface water bodies\nFailing to achieve good ecological status or potential')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'8.Surface_water_bodies_Ecological_status_or_potential_group_Failing{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _8_Surface_water_bodies_Ecological_status_or_potential_group_Good_High(df, country, outfile, imagepath):
    html_string = '''<br>
    '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Country', 'Number']].plot.bar('Country', y=['Number'], rot=0)
        plt.title('Surface water bodies\nHigh-Good')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'8.Surface_water_bodies_Ecological_status_or_potential_group_Good_High{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _8_swEcologicalStatusOrPotential_RW_LW_Category2ndRBMP2016(df, country, outfile, imagepath):
    categories = ["RW", "LW", "TW", "CW", "TeW"]
    ESOPV = df['Ecological Status Or Potential Value'].unique().tolist()
    if not df.loc[(df['Country'] == country)].empty:
        html_string = '''<br>
        '''
        for categ, esopv in zip(categories, ESOPV):

            if not df.loc[(df['Country'] == country) & (df['Surface Water Body Category'] == categ)].empty:
                temp = df.loc[(df['Country'] == country) & (df['Surface Water Body Category'] == categ)]
                html_string += temp.to_html(index=False)
                temp[['Ecological Status Or Potential Value', 'Number']].plot.bar('Ecological Status Or Potential Value',
                                                                                'Number', rot=0)
                plt.title('Surface water bodies\n(' + categ + ')')
                plt.xlabel('Values')
                plt.ylabel('Total Number of\nSurface water bodies')
                plt.gcf()
                plt.draw()
                figfilename = os.path.join(imagepath, f'8.Surface_water_bodies_Ecological_status_or_potential_group_Good_High{country + categ}.png')
                plt.savefig(figfilename, bbox_inches='tight')
                plt.close()
                html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _10_swEcologicalStatusOrPotential_Unknown_Category2ndRBMP2016(df, country, outfile, imagepath):
    html_string = '''<h3>9. Number of surface water bodies at unknown ecological status by category</h3>
    '''
    categories = ["RW", "LW", "TW", "CW"]
    if not df.loc[(df['Country'] == country)].empty:
        for categ in categories:
            if not df.loc[(df['Country'] == country) & (df['Surface Water Body Category'] == categ)].empty:
                temp = df.loc[(df['Country'] == country) & (df['Surface Water Body Category'] == categ)]
                html_string += temp.to_html(index=False)
                temp[['Ecological Status Or Potential Value', 'Number']].plot.bar(
                    'Ecological Status Or Potential Value', 'Number', rot=0)
                plt.title('Surface Water Bodies Categories\nEcological status of potential (' + categ + ')')
                plt.xlabel('')
                plt.ylabel('Total Number of\nSurface water bodies')
                plt.gcf()
                plt.draw()
                figfilename = os.path.join(imagepath, f'10.swEcologicalStatusOrPotential_Unknown_Category2ndRBMP2016{country + categ}.png')
                plt.savefig(figfilename, bbox_inches='tight')
                plt.close()
                html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _12_SurfaceWaterBody_SWB_ChemicalStatus_Table_by_Category2016(df, country, outfile, imagepath):
    categories = df['Surface Water Body Category'].unique().tolist()
    html_string = '''<h3>10. Chemical status of surface water bodies by category</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        for categ in categories:
            if not df.loc[(df['Surface Water Body Category'] == categ) & (df['Country'] == country)].empty:
                temp = df.loc[(df['Surface Water Body Category'] == categ) & (df['Country'] == country)]
                html_string += temp.to_html(index=False)
                temp[['Chemical Status Value', 'Number']].plot.bar('Chemical Status Value', 'Number', rot=0)
                plt.title('Surface water bodies Categories\n' + categ)
                plt.ylabel('Total Number of\nSurface water bodies')
                plt.gcf()
                plt.draw()
                figfilename = os.path.join(imagepath, f'12.SurfaceWaterBody_SWB_ChemicalStatus_Table_by_Category2016{country + categ}.png')
                plt.savefig(figfilename, bbox_inches='tight')
                plt.close()
                html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _12_surfaceWaterBodyChemicalStatusGood2016(df, country, outfile, imagepath):
    html_string = '''<br>
        '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Chemical Status Value', 'Number']].plot.bar('Chemical Status Value', y=['Number'], rot=0)
        plt.title('Surface water bodies\nChemical status')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water body')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'12.surfaceWaterBodyChemicalStatusGood2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _14_swChemical_by_Country(df, country, outfile, imagepath):
    html_string = '''<h3>11. Surface water bodies ecological status or potential and chemical status by country</h3>
    '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Chemical Status Value', 'Number']].plot.bar('Chemical Status Value', 'Number',
                                                                        rot=0)
        plt.title('Surface Water Bodies\nChemical Status')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'14.swChemical_by_Country{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _14_swEcologicalStatusOrPotential_by_Country(df, country, outfile, imagepath):
    html_string = '''<br>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Ecological Status Or Potential Value', 'Number']].plot.bar('Ecological Status Or Potential Value', 'Number',
                                                                        rot=0)
        plt.title('Surface Water Bodies\nEcological status or potential')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'14.swEcologicalStatusOrPotential_by_Country{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _15_swEcologicalStatusOrPotentialValue_swChemicalStatusValue_by_Country_by_Categ(df, country, outfile, imagepath):
    html_string = '''<h3>12. Surface water bodies ecological status or potential and chemical status by category</h3>
    '''
    categories = ["RW", "LW", "TW", "CW", "TeW"]
    if not df.loc[(df['Country'] == country)].empty:
        for categ in categories:
            if not df.loc[(df['Country'] == country) & (df['Categories'] == categ)].empty:
                temp = df.loc[(df['Country'] == country) & (df['Categories'] == categ)]
                html_string += temp.to_html(index=False)
                temp[['Ecological Status Value', 'Number']].plot.bar('Ecological Status Value', 'Number', rot=0)
                plt.title('Surface water bodies Categories\nEcological status')
                plt.xlabel('')
                plt.ylabel('Total Number of\nSurface Water Bodies Category')
                plt.gcf()
                plt.draw()
                figfilename = os.path.join(imagepath, f'_15_swEcologicalStatusOrPotentialValue_swChemicalStatusValue_by_Country_by_Categ{country + categ}.png')
                plt.savefig(figfilename, bbox_inches='tight')
                plt.close()
                html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _15_swChemicalStatusValue_by_Country_by_Categ2016(df, country, outfile, imagepath):
    html_string = '''<br>'''
    categories = ["RW", "LW", "TW", "CW", "TeW"]
    if not df.loc[(df['Country'] == country)].empty:
        for categ in categories:
            if not df.loc[(df['Country'] == country) & (df['Categories'] == categ)].empty:
                temp = df.loc[(df['Country'] == country) & (df['Categories'] == categ)]
                html_string += temp.to_html(index=False)
                temp[['Chemical Status Value', 'Number']].plot.bar('Chemical Status Value', 'Number', rot=0)
                plt.title('Surface water bodies Categories\n(' + categ + ')')
                plt.xlabel('')
                plt.ylabel('Total Number of\nSurface Water Bodies Category')
                plt.gcf()
                plt.draw()
                figfilename = os.path.join(imagepath, f'_15_swChemicalStatusValue_by_Country_by_Categ2016{country + categ}.png')
                plt.savefig(figfilename, bbox_inches='tight')
                plt.close()
                html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _16_Surface_water_bodies_Failing_notUnknown_by_Country2016(df, country, outfile, imagepath):
    html_string = '''<h3>13. % Surface water bodies failing to achieve good status by country</h3>'''
    temp = df.loc[(df['Country'] == country)]
    html_string += temp.to_html(index=False)
    if not df.loc[(df['Country'] == country)].empty:
        temp[['Country', 'Known Status', 'Failing Status']].plot.bar('Country',
                                                                    y=['Known Status', 'Failing Status'], rot=0)
        plt.title('Surface water bodies')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_16_Surface_water_bodies_Failing_notUnknown_by_Country2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _17_Surface_water_bodies_Failing_notUnknown_by_RBD2016(df, country, outfile, imagepath):
    html_string = '''<h3>14. % Surface water bodies failing to achieve good status by country and RBD</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 4:
            temp['Wrap Values'] = temp['RBD Name'].str.wrap(25)
            temp[['Country', 'Wrap Values', 'Known Status', 'Failing Status']].plot.bar('Wrap Values',
                                                                                    y=['Known Status', 'Failing Status'],
                                                                                    rot=0)
        else:
            temp['Wrap Values'] = temp['RBD Name'].str.wrap(30)
            temp[['Country', 'Wrap Values', 'Known Status', 'Failing Status']].plot.bar('Wrap Values',
                                                                                    y=['Known Status', 'Failing Status'],
                                                                                    figsize=(12, 4), rot=80)
        plt.title('Surface water bodies\nFailing status by RBD Name')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_17_Surface_water_bodies_Failing_notUnknown_by_RBD2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _18_GroundWaterBodyCategoryQuantitative_status2016(df, country, outfile, imagepath):
    html_string = '''<h3>15. Groundwater bodies quantitative status</h3>
    '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Quantitative Status Value', 'Area (km^2)']].plot.bar('Quantitative Status Value', y=['Area (km^2)'], rot=0, color="#653700")
        plt.title('Groundwater bodies\nQuantitative status')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_18_GroundWaterBodyCategoryQuantitative_status2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _20_GroundWaterBodyCategoryChemical_status2016(df, country, outfile, imagepath):
    html_string = '''<h3>16. Groundwater bodies chemical status</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Chemical Status Value', 'Area (km^2)']].plot.bar('Chemical Status Value', 'Area (km^2)', rot=0, color="#653700")
        plt.title('Groundwater bodies\nChemical status')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGround water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_20_GroundWaterBodyCategoryChemical_status2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _21_SOW_GWB_gwPollutant_Table2016(df, country, outfile, imagepath):
    html_string = '''<h3>17. Groundwater bodies pollutants and pollutants reported as 'other'</h3>
        '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _21_SOW_GWB_gwPollutant_Table2016_Other(df, country, outfile, imagepath):
    df.dropna()
    html_string = '''<br>'''
    if not df.loc[(df['Country'] == country)].empty:

        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _22_GroundWaterBodyCategoryChemical_status2016(df, country, outfile, imagepath):
    html_string = '''<h3>18. % Groundwater bodies quantitative and chemical status</h3>
    '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Chemical Status Value', 'Area (km^2)']].plot.bar('Chemical Status Value', y=['Area (km^2)'], rot=0, color="#653700")
        plt.title('Groundwater bodies\nChemical status')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_22_GroundWaterBodyCategoryChemical_status2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _22_gwQuantitativeStatusValue_Percent_Country_2016(df, country, outfile, imagepath):
    html_string = '''<br>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Quantitative Status Value', 'Area (km^2)']].plot.bar('Quantitative Status Value', y=['Area (km^2)'], rot=0, color="#653700")
        plt.title('Groundwater bodies\nQuantitative status')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_22_gwQuantitativeStatusValue_Percent_Country_2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _23_Ground_water_bodies_Failing_notUnknown_by_Country2016(df, country, outfile, imagepath):
    html_string = '''<h3>19. % Groundwater bodies failing to achieve good status-country</h3>
            '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Country', 'Known Status', 'Failing status']].plot.bar('Country', y=['Known Status', 'Failing status'], rot=0)
        plt.title('Groundwater bodies')
        plt.xlabel('')
        plt.ylabel('Total Number of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_23_Ground_water_bodies_Failing_notUnknown_by_Country2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _24_Ground_water_bodies_Failing_notUnknown_by_RBD2016(df, country, outfile, imagepath):
    html_string = '''<h3>20. % Groundwater bodies failing to achieve good status-RBD</h3>
                    '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)

        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 4:
            temp['Wrap Value'] = temp['RBD Code'].str.wrap(25)
            temp[['Country', 'Wrap Value', 'Known Status', 'Failing status']].plot.bar('Wrap Value', y=['Known Status', 'Failing status'],
                                                                                rot=0)

        else:
            temp['Wrap Value'] = temp['RBD Code'].str.wrap(30)
            temp[['Country', 'Wrap Value', 'Known Status', 'Failing status']].plot.bar('Wrap Value', y=['Known Status', 'Failing status'],
                                                                                figsize=(12, 4), rot=80)

        plt.title('Groundwater bodies')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_24_Ground_water_bodies_Failing_notUnknown_by_RBD2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _25_Groundwater_bodies_At_risk_of_failing_to_achieve_good_quantitative_status2016(df, country, outfile, imagepath):
    html_string = '''<h3>21. Groundwater bodies at risk of failing to achieve good quantitative status and reasons for failure</h3>
    '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Quantitative Status Value', 'Area (km^2)']].plot.bar('Quantitative Status Value', y=['Area (km^2)'], rot=0, color="#653700")
        plt.title('Groundwater bodies\nQuantitative status')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGround water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_25_Groundwater_bodies_At_risk_of_failing_to_achieve_good_quantitative_status2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _25_SOW_GWB_gwQuantitativeReasonsForFailure_Table2016(df, country, outfile, imagepath):
    if not df.loc[(df['Country'] == country)].empty:
        html_string = '''<br>
        '''
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)

        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 4:
            temp['Wrap Values'] = temp['Quantitative Reasons For Failure'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', y=['Area (km^2)'], rot=0, color="#653700")

        else:
            temp['Wrap Values'] = temp['Quantitative Reasons For Failure'].str.wrap(30)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', y=['Area (km^2)'], figsize=(12, 4), rot=80, color="#653700")

        plt.title('Groundwater bodies\nQuantitative reasons for failure')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGround water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_25_SOW_GWB_gwQuantitativeReasonsForFailure_Table2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _26_gwChemicalStatusValue_Table2016(df, country, outfile, imagepath):
    html_string = '''<h3>22. Groundwater bodies at risk of failing to achieve good chemical status and reasons for failure</h3>
    '''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Chemical Status Value', 'Area (km^2)']].plot.bar('Chemical Status Value', y=['Area (km^2)'], rot=0, color="#653700")
        plt.title('Groundwater bodies\nChemical status')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_26_gwChemicalStatusValue_Table2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _26_SOW_GWB_gwChemicalReasonsForFailure_Table2016(df, country, outfile, imagepath):
    html_string = '''<br>'''

    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Chemical Status Value', 'Area (km^2)']].plot.bar('Chemical Status Value', y=['Area (km^2)'], rot=0, color="#653700")
        plt.title('Groundwater bodies\nChemical reasons for failure')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_26_SOW_GWB_gwChemicalReasonsForFailure_Table2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _29_gwQuantitativeStatusExpectedGoodIn2015(df, country, outfile, imagepath):
    html_string = '''<h3>23. Groundwater bodies good quantitative status expected in 2015</h3>'''

    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 3:

            temp['Wrap Values'] = temp['Quantitative Status Expected Good In 2015'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        rot=0, color="#653700")
        else:
            temp['Wrap Values'] = temp['Quantitative Status Expected Good In 2015'].str.wrap(20)

            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        figsize=(12, 4), rot=80, color="#653700")
        plt.title('Groundwater bodies\nQuantitative status expected good in 2015')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'29.gwQuantitativeStatusExpectedGoodIn2015{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _30_gwQuantitativeStatusExpectedAchievementDate2016(df, country, outfile, imagepath):
    html_string = '''<h3>24. Groundwater bodies good quantitative expected date</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 3:
            temp['Wrap Values'] = temp['Quantitative Status Expected Date'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        rot=0, color="#653700")
        else:
            temp['Wrap Values'] = temp['Quantitative Status Expected Date'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        figsize=(12, 4), rot=80, color="#653700")
        plt.title('Groundwater bodies\nQuantitative status expected date')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'30.gwQuantitativeStatusExpectedAchievementDate2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _31_gwChemicalStatusExpectedGoodIn2015(df, country, outfile, imagepath):
    html_string = '''<h3>25. Groundwater bodies good chemical status expected in 2015</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 3:
            temp['Wrap Values'] = temp['Chemical Status Expected Achievement Date'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        rot=0, color="#653700")
        else:
            temp['Wrap Values'] = temp['Chemical Status Expected Achievement Date'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        figsize=(12, 4), rot=80, color="#653700")
        plt.title('Groundwater bodies\nGood chemical status expected in 2015')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'31.gwChemicalStatusExpectedGoodIn2015{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _32_gwChemicalStatusExpectedAchievementDate2016(df, country, outfile, imagepath):
    html_string = '''<h3>26. Groundwater bodies good chemical expected date</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 3:
            temp['Wrap Values'] = temp['Chemical Status Expected Achievement Date'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        rot=0, color="#653700")
        else:
            temp['Wrap Values'] = temp['Chemical Status Expected Achievement Date'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        figsize=(12, 4), rot=80, color="#653700")
        plt.title('Groundwater bodies\nGood chemical status expected date')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'32.gwChemicalStatusExpectedAchievementDate2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _35_gwQuantitativeAssessmentConfidence2016(df, country, outfile, imagepath):
    html_string = '''<h3>27. Groundwater bodies quantitative status assessment confidence</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 3:
            temp['Wrap Values'] = temp['Quantitative Assessment Confidence'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        rot=0, color="#653700")
        else:
            temp['Wrap Values'] = temp['Quantitative Assessment Confidence'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        figsize=(12, 4), rot=80, color="#653700")
        plt.title('Groundwater bodies\nQuantitative assessment confidence')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'35.gwQuantitativeAssessmentConfidence2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _36_gwChemicalAssessmentConfidence2016(df, country, outfile, imagepath):
    html_string = '''<h3>28. Groundwater bodies chemical status assessment confidence</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 3:
            temp['Wrap Values'] = temp['Chemical Assessment Confidence'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        rot=0, color="#653700")
        else:
            temp['Wrap Values'] = temp['Chemical Assessment Confidence'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        figsize=(12, 4), rot=80, color="#653700")
        plt.title('Groundwater bodies\nChemical assessment confidence')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'36.gwChemicalAssessmentConfidence2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _38_GWB_geologicalFormation2016(df, country, outfile, imagepath):
    html_string = '''<h3>29. Number of groundwater bodies by geological formation</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 3:
            temp['Wrap Values'] = temp['Geological Formation'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        rot=0, color="#653700")
        else:
            temp['Wrap Values'] = temp['Geological Formation'].str.wrap(20)
            temp[['Wrap Values', 'Area (km^2)']].plot.bar('Wrap Values', 'Area (km^2)',
                                                        figsize=(12, 4), rot=80, color="#653700")
        plt.title('Groundwater bodies\nGeological formation')
        plt.xlabel('')
        plt.ylabel('Total Area($km^2$) of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'38.GWB_geologicalFormation2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _39_swb_Chemical_assessment_using_monitoring_grouping_or_expert_judgement2016(df, country, outfile, imagepath):
    CAC = df['Chemical Assessment Confidence'].unique().tolist()

    html_string = '<h3>30. Chemical assessment using monitoring, grouping or expert</h3>'
    for cac in CAC:
        if not df.loc[(df['Country'] == country) & (df['Chemical Assessment Confidence'] == cac)].empty:
            temp = df.loc[(df['Country'] == country) & (df['Chemical Assessment Confidence'] == cac)]
            html_string += temp.to_html(index=False)

            Arguments = df.loc[(df['Country'] == country) & (df['Chemical Assessment Confidence'] == cac)].count()
            if Arguments['Chemical Assessment Confidence'] < 3:
                temp['Wrap Values'] = temp['Chemical Monitoring Results'].str.wrap(25)
                temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'],
                                                    rot=0)
            else:
                temp['Wrap Values'] = temp['Chemical Monitoring Results'].str.wrap(30)
                temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'],
                                                    figsize=(12, 4), rot=80)

            plt.title('Surface water bodies\nChemical assessment confidence')
            plt.xlabel('')
            plt.ylabel('Total Number of\nSurface water bodies')
            plt.gcf()
            plt.draw()
            figfilename = os.path.join(imagepath, f'39.swb_Chemical_assessment_using_monitoring_grouping_or_expert_judgement2016{country + cac}.png')
            plt.savefig(figfilename, bbox_inches='tight')
            plt.close()
            html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _40_swRBsPollutants(df, country, outfile, imagepath):
    html_string = '''<h3>31. River basin specific pollutants and pollutants reported as 'Other'</h3>            '''
    if not df.loc[(df['Country'] == country)].empty:

        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _40_Surface_water_bodies_River_basin_specific_pollutants_reported_as_Other2016(df, country, outfile, imagepath):
    html_string = '''<br>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _42_Surface_water_bodies_QE1_Biological_quality_elements_assessment2016(df, country, outfile, imagepath):
    html_string = '<h3>32. Surface water bodies biological quality elements status</h3>'
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Code', 'Number']].plot.bar('Code', y=['Number'], figsize=[15, 4], rot=80)
        plt.title('Surface water bodies\nBiological quality elements status')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'42.Surface_water_bodies_QE1_Biological_quality_elements_assessment2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _42_Surface_water_bodies_QE2_assessment2016(df, country, outfile, imagepath):
    html_string = '<br>'
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Code', 'Number']].plot.bar('Code', y=['Number'], figsize=[15, 4], rot=80)
        plt.title('Surface water bodies\nHydromorphological quality elements status')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_42_Surface_water_bodies_QE2_assessment2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _42_Surface_water_bodies_QE3_assessment2016(df, country, outfile, imagepath):
    html_string = '<br>'
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Code', 'Number']].plot.bar('Code', y=['Number'], figsize=[15, 4], rot=80)
        plt.title('Surface water bodies\nChemical and physico-chemical quality elements status')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_42_Surface_water_bodies_QE3_assessment2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _42_Surface_water_bodies_QE3_3_assessment2016(df, country, outfile, imagepath):
    html_string = '<br>'
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Code', 'Number']].plot.bar('Code', y=['Number'], figsize=[15, 4], rot=80)
        plt.title('Surface water bodies\nRiver Basin Specific Pollutants status ')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_42_Surface_water_bodies_QE3_3_assessment2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _44_swEcologicalStatusOrPotentialExpectedGoodIn2015(df, country, outfile, imagepath):
    html_string = '''<h3>33. Surface water bodies good ecological status expected in 2015</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 4:
            temp['Wrap Values'] = temp['Ecological Status Or Potential Expected Good In 2015'].str.wrap(20)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'], rot=0)
        else:
            temp['Wrap Values'] = temp['Failing RBSP Other'].str.wrap(20)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'], figsize=(12, 4), rot=80)
        plt.title('Surface water bodies\nEcological status or potential expected good in 2015')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'44.swEcologicalStatusOrPotentialExpectedGoodIn2015{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _45_swEcologicalStatusOrPotentialExpectedAchievementDate2016(df, country, outfile, imagepath):
    html_string = '''<h3>34. Surface water bodies good ecological status expected date</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 4:
            temp['Wrap Values'] = temp['Ecological Status Or Potential Expected Achievement Date'].str.wrap(25)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'], rot=0)
        else:
            temp['Wrap Values'] = temp['Ecological Status Or Potential Expected Achievement Date'].str.wrap(30)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'], figsize=(12, 4), rot=80)
        plt.title('Surface water bodies\nEcological status or potential expected achievement date')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'45.swEcologicalStatusOrPotentialExpectedAchievementDate2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _46_swChemicalStatusExpectedGoodIn2015(df, country, outfile, imagepath):
    html_string = '''<h3>35. Surface water bodies good chemical status expected in 2015</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 4:
            temp['Wrap Values'] = temp['Chemical Status Expected Good In 2015'].str.wrap(25)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'], rot=0)
        else:
            temp['Wrap Values'] = temp['Chemical Status Expected Good In 2015'].str.wrap(30)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'], figsize=(12, 4), rot=80)
        plt.title('Surface water bodies\nChemical status expected good in 2015')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'46.swChemicalStatusExpectedGoodIn2015{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _47_swChemicalStatusExpectedAchievementDate2016(df, country, outfile, imagepath):
    html_string = '''<h3>36. Surface water bodies good chemical status expected date</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        Arguments = df.loc[df['Country'] == country].count()
        if Arguments['Country'] < 4:
            temp['Wrap Values'] = temp['Chemical Status Expected Achievement Date'].str.wrap(20)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'], rot=0)
        else:
            temp['Wrap Values'] = temp['Chemical Status Expected Achievement Date'].str.wrap(30)
            temp[['Wrap Values', 'Number']].plot.bar('Wrap Values', y=['Number'], figsize=(12, 4), rot=80)
        plt.title('Surface water bodies\nChemical status expected achievement date')
        plt.xlabel('')
        plt.ylabel('Total Number of\nSurface water bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'47.swChemicalStatusExpectedAchievementDate2016{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))


def _37_Number_of_groundwater_bodies_failing_to_achieve_good_status(df, country, outfile, imagepath):
    html_string = '''<br><h3>37. Number of groundwater bodies failing to achieve good status</h3>'''
    if not df.loc[(df['Country'] == country)].empty:
        temp = df.loc[(df['Country'] == country)]
        html_string += temp.to_html(index=False)
        temp[['Country', 'Good', 'Failing']].plot.bar(x='Country', y=['Good', 'Failing'], rot=0)
        plt.title('Groundwater bodies\nNumber')
        plt.xlabel('')
        plt.ylabel('Total Number of\nGroundwater bodies')
        plt.gcf()
        plt.draw()
        figfilename = os.path.join(imagepath, f'_37_Number_of_groundwater_bodies_failing_to_achieve_good_status{country}.png')
        plt.savefig(figfilename, bbox_inches='tight')
        plt.close()
        html_string += '<br><img src = "' + figfilename + '"><br>'
    outfile.write(html_string.replace('^2', '<sup STYLE="font-size:75%">2</sup>'))
