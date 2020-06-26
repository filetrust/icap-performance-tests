Sub CreateCharts()
    Dim barChart As Chart
    Dim Name As String
    Dim row As Integer
    Dim interval As Integer
    Dim Hi As Integer
    Dim Wi As Integer
    
    row = 70
    interval = 67
    Hi = 900
    Wi = 1080
    
    'Rows("12:12").Select
    'ActiveWindow.SelectedSheets.HPageBreaks.Add Before:=ActiveCell
    
    'Chart 1 gw-metric-upload
    ActiveSheet.Shapes.AddChart2(208, xlColumnClustered).Select
    Set barChart = ActiveChart
    Name = Replace(barChart.Name, "Sheet1 ", "")
    
    ActiveSheet.Shapes(Name).Height = Hi
    ActiveSheet.Shapes(Name).Width = Wi
    
    With ActiveSheet.Shapes(Name)
        .Left = Range("B" + CStr(row)).Left
        .Top = Range("B" + CStr(row)).Top
    End With

    ActiveChart.SeriesCollection.NewSeries
    ActiveChart.FullSeriesCollection(1).Name = "=Sheet1!$C$1"
    ActiveChart.FullSeriesCollection(1).Values = "=Sheet1!$C$2:$C$41"
    ActiveChart.FullSeriesCollection(1).XValues = "=Sheet1!$L$2:$L$41"
    
    ActiveChart.Axes(xlValue).HasTitle = True
    ActiveChart.Axes(xlValue).AxisTitle.Text = "=Sheet1!$J$1"
    
    ActiveChart.Axes(xlCategory).HasTitle = True
    ActiveChart.Axes(xlCategory).AxisTitle.Text = "=Sheet1!$J$2"
    
    ActiveChart.HasTitle = True
    ActiveChart.ChartTitle.Text = "=Sheet1!$C$1"
    
    ActiveChart.SetElement (msoElementDataLabelOutSideEnd)
    
    row = row + interval
    '
    
    'Chart 2 gw-metric-detect
    ActiveSheet.Shapes.AddChart2(208, xlColumnClustered).Select
    Set barChart = ActiveChart
    Name = Replace(barChart.Name, "Sheet1 ", "")
    
    ActiveSheet.Shapes(Name).Height = Hi
    ActiveSheet.Shapes(Name).Width = Wi
    
    With ActiveSheet.Shapes(Name)
        .Left = Range("B" + CStr(row)).Left
        .Top = Range("B" + CStr(row)).Top
    End With

    ActiveChart.SeriesCollection.NewSeries
    ActiveChart.FullSeriesCollection(1).Name = "=Sheet1!$D$1"
    ActiveChart.FullSeriesCollection(1).Values = "=Sheet1!$D$2:$D$41"
    ActiveChart.FullSeriesCollection(1).XValues = "=Sheet1!$L$2:$L$41"
    
    ActiveChart.Axes(xlValue).HasTitle = True
    ActiveChart.Axes(xlValue).AxisTitle.Text = "=Sheet1!$J$1"
    
    ActiveChart.Axes(xlCategory).HasTitle = True
    ActiveChart.Axes(xlCategory).AxisTitle.Text = "=Sheet1!$J$2"
    
    ActiveChart.HasTitle = True
    ActiveChart.ChartTitle.Text = "=Sheet1!$D$1"
    
    ActiveChart.SetElement (msoElementDataLabelOutSideEnd)
    
    row = row + interval
    '
    
    'Chart 3 gw-metric-download
    ActiveSheet.Shapes.AddChart2(208, xlColumnClustered).Select
    Set barChart = ActiveChart
    Name = Replace(barChart.Name, "Sheet1 ", "")
    
    ActiveSheet.Shapes(Name).Height = Hi
    ActiveSheet.Shapes(Name).Width = Wi
    
    With ActiveSheet.Shapes(Name)
        .Left = Range("B" + CStr(row)).Left
        .Top = Range("B" + CStr(row)).Top
    End With

    ActiveChart.SeriesCollection.NewSeries
    ActiveChart.FullSeriesCollection(1).Name = "=Sheet1!$E$1"
    ActiveChart.FullSeriesCollection(1).Values = "=Sheet1!$E$2:$E$41"
    ActiveChart.FullSeriesCollection(1).XValues = "=Sheet1!$L$2:$L$41"
    
    ActiveChart.Axes(xlValue).HasTitle = True
    ActiveChart.Axes(xlValue).AxisTitle.Text = "=Sheet1!$J$1"
    
    ActiveChart.Axes(xlCategory).HasTitle = True
    ActiveChart.Axes(xlCategory).AxisTitle.Text = "=Sheet1!$J$2"
    
    ActiveChart.HasTitle = True
    ActiveChart.ChartTitle.Text = "=Sheet1!$E$1"
    
    ActiveChart.SetElement (msoElementDataLabelOutSideEnd)
    
    row = row + interval
    '
    
    'Chart 4 gw-metric-rebuild
    ActiveSheet.Shapes.AddChart2(208, xlColumnClustered).Select
    Set barChart = ActiveChart
    Name = Replace(barChart.Name, "Sheet1 ", "")
    
    ActiveSheet.Shapes(Name).Height = Hi
    ActiveSheet.Shapes(Name).Width = Wi
    
    With ActiveSheet.Shapes(Name)
        .Left = Range("B" + CStr(row)).Left
        .Top = Range("B" + CStr(row)).Top
    End With

    ActiveChart.SeriesCollection.NewSeries
    ActiveChart.FullSeriesCollection(1).Name = "=Sheet1!$F$1"
    ActiveChart.FullSeriesCollection(1).Values = "=Sheet1!$F$2:$F$41"
    ActiveChart.FullSeriesCollection(1).XValues = "=Sheet1!$L$2:$L$41"
    
    ActiveChart.Axes(xlValue).HasTitle = True
    ActiveChart.Axes(xlValue).AxisTitle.Text = "=Sheet1!$J$1"
    
    ActiveChart.Axes(xlCategory).HasTitle = True
    ActiveChart.Axes(xlCategory).AxisTitle.Text = "=Sheet1!$J$2"
    
    ActiveChart.HasTitle = True
    ActiveChart.ChartTitle.Text = "=Sheet1!$F$1"
    
    ActiveChart.SetElement (msoElementDataLabelOutSideEnd)
    '
    
End Sub