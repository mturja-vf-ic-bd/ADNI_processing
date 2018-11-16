#include <string.h>
#include <string>
#include <iostream>
#include <map>
#include <iterator>

#include <vtkSmartPointer.h>
#include <vtkCellData.h>
#include <vtkMath.h>
#include <vtkIntArray.h>
#include <vtkStringArray.h>
#include <vtkPoints.h>
#include <vtkPolyData.h>
#include <vtkPointData.h>
#include <vtkFieldData.h>
#include <vtkSphereSource.h>
#include <vtkPolyDataReader.h>
#include <vtkPolyDataWriter.h>
#include <vtkDelimitedTextReader.h>
#include <vtkTable.h>
#include <vtkAppendPolyData.h>

int main(int argc, char *argv[])
{
    // Input
    // Verify input arguments
    if ( argc != 4 )
    {
        std::cout << "Usage: " << argv[0]
                  << " updateParcellationTable.cxx" << std::endl;
        return EXIT_FAILURE;
    }

    std::string oldParcellationTable = strdup(argv[1]); //parcellation table that we want to update
    std::string surface = strdup(argv[2]);              // vtk file of the surface
    int debug = std::stoi(strdup(argv[3]));

    // Read file
    vtkSmartPointer<vtkPolyDataReader> polyIn = vtkSmartPointer<vtkPolyDataReader>::New();
    polyIn->SetFileName(surface.c_str()); 
    polyIn->Update();
    vtkSmartPointer<vtkPolyData> polydata = polyIn->GetOutput();
    unsigned int nPoints = polydata->GetNumberOfPoints();
    unsigned int numberOfArrays = polydata->GetPointData()->GetNumberOfArrays();
    
    for (vtkIdType id = 0; id < nPoints; id++) {
        cout << polydata->GetPoint(id) << endl;
    }

    return EXIT_SUCCESS;
}