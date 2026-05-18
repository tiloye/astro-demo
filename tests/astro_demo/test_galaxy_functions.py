import pandas as pd
from astro_demo.galaxy_functions import get_galaxy_data


class TestGetGalaxyData:
    """Test suite for the get_galaxy_data function."""

    def test_returns_dataframe(self):
        """Test that get_galaxy_data returns a pandas DataFrame."""
        result = get_galaxy_data()
        assert isinstance(result, pd.DataFrame)

    def test_default_returns_20_galaxies(self):
        """Test that default call returns 20 galaxies."""
        result = get_galaxy_data()
        assert len(result) == 20

    def test_custom_number_of_galaxies(self):
        """Test that custom num_galaxies parameter works correctly."""
        result = get_galaxy_data(num_galaxies=5)
        assert len(result) == 5

        result = get_galaxy_data(num_galaxies=10)
        assert len(result) == 10

    def test_required_columns_present(self):
        """Test that all required columns are present in the DataFrame."""
        result = get_galaxy_data(num_galaxies=1)
        required_columns = [
            "name",
            "distance_from_milkyway",
            "distance_from_solarsystem",
            "type_of_galaxy",
            "characteristics",
        ]
        for col in required_columns:
            assert col in result.columns

    # def test_data_types(self):
    #     """Test that columns have the correct data types."""
    #     result = get_galaxy_data(num_galaxies=1)
    #     assert result["name"].dtype == "object"
    #     assert pd.api.types.is_numeric_dtype(result["distance_from_milkyway"])
    #     assert pd.api.types.is_numeric_dtype(result["distance_from_solarsystem"])
    #     assert result["type_of_galaxy"].dtype == "object"
    #     assert result["characteristics"].dtype == "object"

    def test_no_null_values(self):
        """Test that there are no null values in the returned data."""
        result = get_galaxy_data()
        assert not result.isnull().any().any()

    def test_known_galaxies_present(self):
        """Test that known galaxies are in the dataset."""
        result = get_galaxy_data(num_galaxies=20)
        galaxy_names = result["name"].tolist()
        expected_galaxies = [
            "Andromeda Galaxy",
            "Large Magellanic Cloud",
            "Small Magellanic Cloud",
            "Canis Major Dwarf",
        ]
        for galaxy in expected_galaxies:
            assert galaxy in galaxy_names

    def test_distance_values_are_positive(self):
        """Test that all distance values are positive."""
        result = get_galaxy_data()
        assert (result["distance_from_milkyway"] > 0).all()
        assert (result["distance_from_solarsystem"] > 0).all()

    def test_galaxy_types_are_valid(self):
        """Test that galaxy types are from expected categories."""
        result = get_galaxy_data(num_galaxies=20)
        valid_types = ["Dwarf", "Dwarf Spheroidal", "Irregular", "Spiral"]
        assert result["type_of_galaxy"].isin(valid_types).all()

    # def test_large_number_returns_max_20(self, capsys):
    #     """Test that requesting more than 20 galaxies caps at 20."""
    #     result = get_galaxy_data(num_galaxies=100)
    #     assert len(result) == 20
    #     # Verify warning message is printed
    #     captured = capsys.readouterr()
    #     assert "maximum number galaxies for which data can be returned is 20" in captured.out

    def test_zero_galaxies(self):
        """Test requesting zero galaxies."""
        result = get_galaxy_data(num_galaxies=0)
        assert len(result) == 0
        assert isinstance(result, pd.DataFrame)

    def test_andromeda_galaxy_data(self):
        """Test specific data for Andromeda Galaxy."""
        result = get_galaxy_data(num_galaxies=20)
        andromeda = result[result["name"] == "Andromeda Galaxy"]
        assert not andromeda.empty
        assert andromeda["distance_from_milkyway"].values[0] == 2540000
        assert andromeda["type_of_galaxy"].values[0] == "Spiral"
        assert "collide" in andromeda["characteristics"].values[0].lower()

    # def test_canis_major_is_closest(self):
    #     """Test that Canis Major Dwarf is the closest galaxy."""
    #     result = get_galaxy_data(num_galaxies=20)
    #     canis_major = result[result["name"] == "Canis Major Dwarf"]
    #     assert not canis_major.empty
    #     min_distance = result["distance_from_milkyway"].min()
    #     assert canis_major["distance_from_milkyway"].values[0] == min_distance
